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

#save processed datasets to conserve memory later
from numpy import asarray
from numpy import save
from numpy import load
import joblib #to save models

from keras.models import load_model








train_x = load('savedModels/train_x.npy')
#train_y = load('savedModels/train_y.npy')
test_x = load('savedModels/test_x.npy')




"""

n_inputs = 77

# define encoder
visible = Input(shape=(n_inputs,))
# encoder level 1
e = Dense(n_inputs*2)(visible)
e = BatchNormalization()(e)
e = LeakyReLU()(e)
# encoder level 2
e = Dense(n_inputs)(e)
e = BatchNormalization()(e)
e = LeakyReLU()(e)
# bottleneck
n_bottleneck = round(float(n_inputs) / 2.0)
#n_bottleneck = n_inputs
bottleneck = Dense(n_bottleneck)(e)


# define decoder, level 1
d = Dense(n_inputs)(bottleneck)
d = BatchNormalization()(d)
d = LeakyReLU()(d)
# decoder level 2
d = Dense(n_inputs*2)(d)
d = BatchNormalization()(d)
d = LeakyReLU()(d)
# output layer
output = Dense(n_inputs, activation='linear')(d)





"""



"""

# define autoencoder models


model = Model(inputs=visible, outputs=output)
# compile autoencoder model
model.compile(optimizer='adam', loss='mse')
# plot the autoencoder
plot_model(model, 'autoencoder_half_compress.png', show_shapes=True)
# fit the autoencoder model to reconstruct input
history = model.fit(train_x, train_x, epochs=15, batch_size=120, verbose=2, validation_data=(test_x, test_x))
# plot loss
pyplot.plot(history.history['loss'], label='train')
pyplot.plot(history.history['val_loss'], label='test')
pyplot.legend()
pyplot.show()
# define an encoder model (without the decoder)
encoder = Model(inputs=visible, outputs=bottleneck)
plot_model(encoder, 'encoder_compress.png', show_shapes=True)
# save the encoder to file
encoder.save('encoder_bottleneck_half.h5')

"""



# logistic regression model
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score





train_x = load('savedModels/train_x.npy', allow_pickle=True)
train_y = load('savedModels/train_y.npy', allow_pickle=True)

test_x = load('savedModels/test_x.npy', allow_pickle=True)
test_y = load('savedModels/test_y.npy', allow_pickle=True)





# load the model from file
encoder = load_model('encoder_bottleneck_half.h5')

# encode the train data
X_train_encode = encoder.predict(train_x)

# encode the test data
X_test_encode = encoder.predict(test_x)

# define the model
model = LogisticRegression()

# fit the model on the training set
model.fit(X_train_encode, train_y)

# make predictions on the test set
yhat = model.predict(X_test_encode)

import pickle
pickle.dump(model, open("classifer2.pkl", "wb"))


"""
# load the model
model = pickle.load(open("classifer2.pkl", "rb"))



# calculate classification accuracy
acc = accuracy_score(test_y, yhat)
print(acc)
"""
