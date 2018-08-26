from sklearn import datasets

import numpy as np
from lms import lms_regression as lms
from sklearn import linear_model

# The data
boston = datasets.load_boston()
X = boston.data
Y = boston.target
m = X.shape[0]

# Normalization of data
X_train = (X-X.min(axis=0))/(X.max(axis=0)-X.min(axis=0))
Y_train = (Y-Y.min())/(Y.max()-Y.min())
#X_train = (X-X.mean(axis=0))/X.std(axis=0)
#Y_train = Y #(Y-Y.mean())/Y.std()

# Put in shape for normal equations
X_train = np.hstack([np.ones([m,1]), X_train])
Y_train = Y_train.reshape(m,1)

# Direct Solution
theta = np.linalg.solve(np.dot(X_train.T, X_train), np.dot(X_train.T, Y_train))
print theta

# sklearn solution
regr = linear_model.LinearRegression()
regr.fit(X_train, Y_train) # Still must add the column of 1
theta = regr.coef_
print theta

# LMS Solution
theta0 = Y_train.mean()/X_train.mean(axis=0)/X.shape[1]
theta = lms(X_train, Y_train, theta0)
print theta

