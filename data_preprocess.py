#from sklearn.datasets import make_classification
#from sklearn.model_selection import train_test_split
#import array as arr
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np





class data_preprocessing():
    
    def __init__ (self):
        self.current_directory = ""
       
        self.df = pd.DataFrame(list())
        
        self.train_x = pd.DataFrame(list())
        self.train_y = pd.DataFrame(list())
        self.text_x = pd.DataFrame(list())
        self.test_y = pd.DataFrame(list())
        
        
    def get_data(self, file_path):
        
        df = pd.read_csv(file_path, index_col=False)
        return df



    def set_data(self, df):
        self.df = df
        

    #used for splitting data into testing/training sets **for trainings the ML models**
    #dont use once app is running
    def split_data(self, df_inp = pd.DataFrame(list())):
        
        if (len(self.df) == 0):
            self.df = df_inp
            
        if(len(self.df) == 0):
            return "no dataframe available/provided => cannot perform the operation"
        
        else:
            from sklearn.model_selection import train_test_split
            
            training_data, testing_data = train_test_split(self.df, test_size=0.2, random_state=25)
            
            training_data = self.remove_non_numeric(training_data)
            testing_data = self.remove_non_numeric(testing_data)
            
            #feature extraction (get all columns except for the last one)
            self.test_x = testing_data.iloc[:,:-1].values
            self.train_x = training_data.iloc[:,:-1].values
            print(testing_data)
            #label extraction (get the 41st column only)
            self.test_y = testing_data.iloc[:,78].values
            self.train_y = training_data.iloc[:,78].values



    #removes any rows that contain non numeric or infinity values
    def remove_non_numeric(self, df):

        new_df = df[~df.isin([np.nan, np.inf, -np.inf]).any(axis=1)]
        return new_df
    
 
    def scale_data(self, df, scale = 0):
        #from sklearn.preprocessing import StandardScaler 
        
        #used to properly scale the data
        if scale == 1:
            df.to_csv('flow_scale_process.csv', header=False, index=False)
            df = pd.read_csv("flow_scale_process.csv", header=None)
            df_min_max = pd.read_csv("df_min_max.csv", header=None)
            #df = df.append(df_min_max)
            df = pd.concat([df, df_min_max])
    
        #st_x= StandardScaler()  
        st_x = MinMaxScaler()

        df = st_x.fit_transform(df)
        df = st_x.transform(df)
        
        df = pd.DataFrame(df)
        
        # remove extra rows used for min-max scaling
        if scale == 1:
            df = df.iloc[:-2]
        
        return df



    # Transform the classification labels from text to numeric
    def label_encode(self):
        from sklearn.preprocessing import LabelEncoder, OneHotEncoder
        from sklearn.compose import ColumnTransformer
        labelencoder_X = LabelEncoder()
        self.train_y= labelencoder_X.fit_transform(self.train_y)
        self.test_y= labelencoder_X.fit_transform(self.test_y)


    #save processed datasets to conserve memory later
    def save_data(self):
        from numpy import asarray
        from numpy import save
        
        save('savedModels/train_x.npy', self.train_x)
        save('savedModels/train_y.npy', self.train_y)
        
        save('savedModels/test_x.npy', self.test_x)
        save('savedModels/test_y.npy', self.test_y)











