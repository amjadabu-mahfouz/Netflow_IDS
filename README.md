# Setting Up
Your environment should have Tensorflow and Keras installed
Need to install the cicflowmeter module 
1. Make sure there are no duplicates/conflicts by uninstalling all existing cicflowmeter modules
	
```
pip uninstall cicflowmeter
pip3 uninstall cicflowmeter
```
	
2. Clone the Github cicflowmeter repo	
```
git clone https://gitlab.com/hieulw/cicflowmeter
```
			
3. Go inside the cicflowmeter folder and run the setup 
```
cd cicflowmeter
python setup.py install
```
			
4. If cicflowmeter is installed using pip, you may get a type mismatch error; in which case you will need to go into the flows.py file in the cicflowmeter 	site-package and replace the decimal casts with float casts in the lines that the error appears 
	
- Numpy should be upgraded to version over 1.3.0 otherwise replace line 47 with line 46 in IDS_main.py
	
	

# How to Use
1. Switch to your keras environment
	
2) Go into the project folder
	
3) Find the network interface you are using
In Windows command line:
```
ipconfig
```
In Linux command line:
```
ifconfig
```
		
4. If running on command line use the following command with whatever interface you want to listen at after the -i option. use <ctrl + Pause Break> to end the program
```
python IDS.py -i Wi-Fi
```
If running through the python interpreter, then open the IDS.py file and enter the interface you want to use as a string parameter into the IDS_core class
```
IDS_core('Wi-Fi')
```
-sometimes the cicflowmeter will display errors in the command line during runtime, ignore them as they would not interfere with the program execution.
		
#Program Components

	IDS_main.py: the main body of this project is in this file
		This module consists of 2 threads that run concurrently. 
			Thread 1 periodically checks if flows are entered into the flows2.csv file, once it detects flows 
			it will process the csv file by removing the unused fields and non-numeric rows, scale the data, and used the trained AE model to predict if the flows exhibit a malicious signature. 
			The malicious flows are logged into the maliciousFlows.csv file.

			Thread 2 will run the imported cicflowmeter and will update the flows2.csv file so it could be used by thread 1.  
			
			
	data_Preprocess.py: this is the data preprocessing module and is mainly used the the IDS_main.py module to scale and remove the non numeric data. 
	
	csv_editor.py: this module is used to rearrange the columns in the passed csv file, create and save csv files, and delete certain columns so the dataset would match the ones collected by the cicflowmeter
	
	data_prep.py: this was used for preparing the dataset to be used for training
	
	model_setup.py: used for training the autoencoder model and classifier models.
			the models are trained using the CICIDS2017 dataset where all weekday sets were concatenated into a massive dataset. please refer to the original source for more information in the link below.
			https://www.unb.ca/cic/datasets/ids-2017.html#:~:text=The%20CICIDS2017%20dataset%20consists%20of,are%20publicly%20available%20for%20researchers.
	
	
	
