# -*- coding: utf-8 -*-
"""HW4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tG9lRuZ52mhALHcLnC7DBeh_VUQ0wV_A
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import confusion_matrix, accuracy_score
import keras as keras
from keras.models import Sequential
from keras.layers import Dense, Activation
from datascience import *
import matplotlib.pyplot as plt
# %matplotlib inline

from google.colab import files
uploaded = files.upload()

data = pd.read_csv("Admissions.csv")
data.head()
# DATA = Table.read_table("Admissions.csv")
# DATA.show(3)
# DATA.scatter('rank','gpa', colors = 2)

features = data[['gre','gpa','rank']]
features[0:5]

TARGET = data[['admit']]
TARGET[0:5]

# SCALE PREDICTOR between 0 and 1
featuresSCALED = preprocessing.minmax_scale(data[['gre','gpa','rank']])
featuresSCALED[0:5]
plt.scatter(featuresSCALED[:,0], featuresSCALED[:,1])
plt.xlabel("gre")
plt.ylabel("gpa")
plt.show()

print(TARGET[:5])

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelBinarizer

# ENCODE the RESPONSE VARIABLE
TARGETS = np.array(data["admit"])
print(TARGETS[0:5])
print(type(TARGETS))

TARGETS_onehot  = pd.get_dummies(TARGETS)
TARGETShot = np.array(TARGETS_onehot)
print(TARGETShot[0:5,:])

# PRINTING again the PREDICTORS and the RESPONSE variables 
print(type(featuresSCALED))
print(featuresSCALED.shape)
print(featuresSCALED[:5,:])

print(type(TARGETShot))
print(TARGETShot.shape)
print(TARGETShot[:5])

# here to make the NEURAL NETWORK MODEL
features = featuresSCALED
output = TARGETShot

features_shape = features.shape[1]
print(features_shape)

output_shape = output.shape[1]
print(output_shape)

# STARTING with the NUMBER of HIDDEN LAYERS
# the NUMBER of HIDDEN LAYES
hidden_nodes = 5

from sklearn.model_selection import train_test_split

RANDOM_SEED = 1234
TRAIN_features, TEST_features, TRAIN_output, TEST_output = train_test_split(featuresSCALED, output, test_size=0.33, random_state = RANDOM_SEED)

# here making the NEURAL NETWORK in KERAS
model = Sequential()
model.add(Dense(hidden_nodes, input_dim = features_shape, activation = "relu"))
model.add(Dense(output_shape, activation = "softmax"))

model.compile(loss="categorical_crossentropy", optimizer = "adam")
model.summary()

# training the model 
epochs = 1000
hist = model.fit(TRAIN_features, TRAIN_output, epochs = epochs, batch_size = 128, verbose=0 )

# in order to visualize the LOSSES

training_loss = hist.history["loss"]
xc = range(epochs)
plt.plot(xc, training_loss)
plt.xlabel("number of epochs")
plt.ylabel("loss")
plt.title("training_loss")
plt.grid(True)
plt.style.use(["ggplot"])

# PRINT the values of all the weights and bias of all the neurons of the Neural Network

for layerNum, layer in enumerate(model.layers):
    print("Weights Values = ")
    weights = layer.get_weights()[0]
    print(weights)
    print("Bias Values = ")
    biases = layer.get_weights()[1]
    print(biases)
    print("                      ")

# here predicting the outcome of the TEST_FEATURES

PREDICTIONS = model.predict(TEST_features)
predictClass = np.argmax(PREDICTIONS, axis=1)
print(predictClass)

# the values of the TEST_OUTPUT

the_OUTPUT_of_the_MODEL = np.argmax(TEST_output, axis =1)
print(the_OUTPUT_of_the_MODEL)

# BUILDING the CONFUSION MATRIX
CM = confusion_matrix(predictClass, the_OUTPUT_of_the_MODEL)
print(CM)
print("Accuracy Score:", accuracy_score(predictClass, the_OUTPUT_of_the_MODEL))



