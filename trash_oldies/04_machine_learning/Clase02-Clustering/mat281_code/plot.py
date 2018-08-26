from matplotlib import pyplot as plt
import numpy as np
from pdb import set_trace as st

colors = ["r", "b", "g", "c", "k", "y", "m"]

def resize(X):
    Xmin = X[:].min()
    Xmax = X[:].max()
    dX = .1*(Xmax-Xmin)
    plt.xlim([Xmin-dX, Xmax+dX])
    plt.ylim([Xmin-dX, Xmax+dX])
    return

def data(X):
    plt.figure(figsize=(12,6))
    plt.plot(X[:,0], X[:,1],'ko')
    resize(X)
    plt.show()
    return

def clusters(X, centroids, clusters):
    plt.figure(figsize=(12,6))
    for j in range(len(centroids)):
        c = colors[j%len(colors)]
        mu = centroids[j]
        C = X[clusters==j]
        plt.plot(C[:,0], C[:,1], c+'o')
        plt.plot(mu[0], mu[1], 'w*', ms=16, mew=2.0)
    resize(X)
    plt.show()
    return
