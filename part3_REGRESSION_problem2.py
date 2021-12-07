# -*- coding: utf-8 -*-
"""HW3_PROBLEM2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LA7nsciH3NUnLPBpcNigajUd9tDST5X_
"""

# the SOLUTION with SKLEARN

import numpy as np 
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import preprocessing
import pandas as pd

from google.colab import files 
uploaded = files.upload()

data = pd.read_csv("00 kc_house_data.csv")
print(data.head(), "\n\n")

F = data[["bedrooms", "sqft_living", "price"]]
# have SCALED the DATA using MINMAX FEATURE
# essentially, we do use NORMALIZED DATA
FS = preprocessing.minmax_scale(F)
print(type(FS))
FS[0:3]

x = FS[:, 0:2]
y = FS[:, 2]

# in order to display the NORMALIZED DATA
# adapting the code from SLIDE 29
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

axis1 = FS[:, 0]
axis2 = FS[:, 1]
axis3 = FS[:, 2]

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(axis1, axis2, axis3, c="blue", marker ="o", alpha = 0.5)
ax.set_xlabel("bedrooms")
ax.set_ylabel("sqft_living")
ax.set_zlabel("price")
plt.show()

linreg = linear_model.LinearRegression()
linreg.fit(x, y) 
print(linreg.intercept_)
print(linreg.coef_)

# THE SOLUTION PROVIDED with KERAS

import keras 
from keras.models import Sequential 
from keras.layers import Dense

# we have defined above 
# x = FS[:, 0:2]
# y = FS[:, 2]
# we tra

xx = np.array(x)
yy = np.array(y)

# We already work with NORMALIZED/MIN_MAX SCALED VALUES

model = Sequential()
model.add(Dense(1, input_dim=2, kernel_initializer = "normal", activation = "linear"))

# compile the MODEL
model.compile(loss = "mean_squared_error", optimizer = "adam", metrics = ["mse"])

model.summary()

# epochs = 10000
epochs = 1000
hist = model.fit(xx, yy, epochs = epochs, verbose=0)

# get Regression Weights
weightBias = model.layers[0].get_weights()
print("Weights + Bias = ", weightBias)

# visualizing the LOSSES
# in this case 1000 epochs did suffice in order to reach the CONVERGENCE

train_loss = hist.history["loss"]
range_epochs = range(epochs)
plt.plot(range_epochs, train_loss)


plt.figure(1, figsize = (7,5))
plt.xlabel("num of epochs")
plt.ylabel("loss")
plt.title("trains_loss")
# plt.grid(True)
# plt.style.use(["ggplot"])
