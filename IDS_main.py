import os
import pandas as pd
import pickle
from keras.models import load_model
import threading
import subprocess
from threading import Event
from csv_editor import ChangeCsv
from data_preprocess import data_preprocessing 



class IDS_core:
   
    def __init__ (self, interface):
        self.exit = Event()
        self.csv_edit = ChangeCsv()
        self.newDP = data_preprocessing()
        
        # load the encoder model from file
        self.encoder = load_model('encoder_bottleneck_half.h5')
        # load the model
        self.model = pickle.load(open("classifer2.pkl", "rb"))
      
        self.func1_loop = 1
        self.func2_loop = 1
        
        self.process = subprocess.Popen
        print("Listening on following interface: " + str(interface))
        self.interface = interface

        self.start_ids()


    def function_1(self):

       while(self.func1_loop):
            #print('new iteration')
            #30 second timer between cheking for new flows
            self.exit.wait(30)

            if(os.stat("flows2.csv").st_size == 0):
                print("No flows found at the moment...")
            else:
                #df = pd.read_csv("flows2.csv",  index_col=False)
                #df = pd.read_csv("flows2.csv", error_bad_lines=False, index_col=False) #for numpy version < 1.3.0
                df = pd.read_csv("flows2.csv", on_bad_lines='skip', index_col=False)
                
                if(df.columns[0] == "src_ip"):
                    print("Generated flows found: ")
                    #remove extra columns to match dataset of trained model
                    df = self.csv_edit.removeColumns(df)
        
                    #remove the rows with non-numeric data thenscale the data
                    df = self.newDP.remove_non_numeric(df)
                    df = self.newDP.scale_data(df, 1)
                    
                    #encode then predict using classifier model
                    encoded = self.encoder.predict(df)
                    predicted = self.model.predict(encoded)
                    
                    row_num = 0
                    for s in predicted:
                        if s != 'BENIGN':
                            print("Potential threat!: " + s + " signature")
                            self.csv_edit.createCSVFile("append", df.iloc[[row_num]], 1, "maliciousFlows.csv")
                        row_num += 1
                    
                    #log recieved flows    
                    #csv_edit.createCSVFile("append", df, 1)
                    
                    print("Refreshing thread2")
                    self.process.kill()
                
        
    
    def function_2(self):
       #print("generating flows ....")
       #os.system('cicflowmeter -i Ethernet -c flows2.csv')
        while(self.func2_loop):
            print("generating flows ....")
            self.process = subprocess.Popen('cicflowmeter -i '+self.interface+' --csv flows2.csv')
            self.process.wait()


    def start_ids(self):
        # Create a new thread => for checking, processing, and testing network flows 
        Thread1 = threading.Thread(target=self.function_1)
        
        # Create another new thread => for running cicflowmeter to capture network flows
        Thread2 = threading.Thread(target=self.function_2)

        # Start the threads
        Thread2.start()
        Thread1.start()
        
        # Wait for the threads to finish
        Thread1.join()
        Thread2.join()
  

