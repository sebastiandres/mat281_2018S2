import numpy as np
from scipy.linalg import norm

from pdb import set_trace as st

def find_centers(X, k, seed=None):
    if not seed:
      seed = np.random.randint(10000000)
    np.random.seed(seed)
    # Initialize to K random centers
    old_centroids = random_centers(X, k)
    new_centroids = random_centers(X, k)
    while not has_converged(new_centroids, old_centroids):
        old_centroids = new_centroids
        # Assign all points in X to clusters
        clusters = cluster_points(X, old_centroids)
        # Reevaluate centers
        new_centroids = reevaluate_centers(X, clusters, k)
    return (new_centroids, clusters)

def random_centers(X, k):
    index = np.random.randint(0, X.shape[0], k)
    return X[index, :]

def has_converged(new_mu, old_mu, tol=1E-6):
    num = norm(np.array(new_mu)-np.array(old_mu))
    den = norm(new_mu)
    rel_error= num/den
    return rel_error < tol

def cluster_points(X, centroids):
    clusters = []
    for i, x in enumerate(X):
        distances = np.array([norm(x-cj) for cj in centroids])
        clusters.append( distances.argmin())
    return np.array(clusters)

def reevaluate_centers(X, clusters, k):
    centroids = []
    for j in range(k):
        cj = X[clusters==j,:].mean(axis=0)
        centroids.append(cj)
    return centroids
