from sklearn.datasets import make_classification
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LeakyReLU
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.utils import plot_model
from matplotlib import pyplot
import pandas as pd
import numpy as nm

import tensorflow as tf

import numpy as np
import array as arr
import tensorflow as tf


from csv_editor import ChangeCsv

csv_edit = ChangeCsv()



from CSVeditor import ChangeCsv
csv_edit = ChangeCsv()


#get dataset
df = pd.read_csv('dataset/cicflow2017/TRAIN_FINAL.csv')
#df = df.reset_index()

#df = csv_edit.removeColumns(df)


#drop any nan  or inf rows
#df[~df.isin([np.nan, np.inf, -np.inf]).any(1)]


from sklearn.model_selection import train_test_split

training_data, testing_data = train_test_split(df, test_size=0.2, random_state=25)

training_data = training_data[~training_data.isin([np.nan, np.inf, -np.inf]).any(1)]
testing_data = testing_data[~testing_data.isin([np.nan, np.inf, -np.inf]).any(1)]


#feature extraction (get all columns except for the last one)
test_x = testing_data.iloc[:,:-1].values
train_x = training_data.iloc[:,:-1].values

#label extraction (get the last column only)
test_y = testing_data.iloc[:,77].values
train_y = training_data.iloc[:,77].values


from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
labelencoder_X = LabelEncoder()
train_y2= labelencoder_X.fit_transform(train_y)
test_y2= labelencoder_X.fit_transform(test_y)





#from sklearn.preprocessing import StandardScaler 
 
#st_x= StandardScaler()  
st_x = MinMaxScaler()

train_x= st_x.fit_transform(train_x)
test_x= st_x.transform(test_x) 


from numpy import asarray
from numpy import save
        
save('savedModels/train_x.npy', train_x)
save('savedModels/train_y.npy', train_y)

save('savedModels/test_x.npy', test_x)
save('savedModels/test_y.npy', test_y)













