from sklearn import datasets

# The data
boston = datasets.load_boston()
X = boston.data
Y = boston.target

# What's the data
print X.DESCR
