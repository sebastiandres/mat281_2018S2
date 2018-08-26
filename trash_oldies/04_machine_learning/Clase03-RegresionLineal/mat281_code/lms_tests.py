import numpy as np
from sklearn import datasets
from lms import lms_regression as lms

# The data
boston = datasets.load_boston()
X = boston.data
Y = boston.target
m, n = X.shape

# Normalization of data
#X = (X-X.min(axis=0))/(X.max(axis=0)-X.min(axis=0))
#Y = (Y-Y.min())/(Y.max()-Y.min())
X = np.hstack([np.ones([m,1]), X])
Y = Y.reshape(m,1)


# LMS Solution
#theta0 = Y.mean()/X.mean(axis=0)/n
#print theta0
#theta = lms(X, Y, theta0)
#print theta

# Direct Solution
theta = np.linalg.solve(np.dot(X.T, X), np.dot(X.T, Y))
print theta

