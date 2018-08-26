from IPython.html.widgets import interact
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.datasets.samples_generator import make_blobs

import matplotlib.pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings('ignore')

def kmeans(N_points=300, n_clusters=4):

    X, y = make_blobs(n_samples=N_points, centers=n_clusters,
                      random_state=0, cluster_std=0.60)

    def _kmeans_step(k=n_clusters, frame=0):
        rng = np.random.RandomState(2)
        labels = np.zeros(X.shape[0])
        centers = X[rng.randint(N_points, size=k),:]

        nsteps = frame // 3

        for i in range(nsteps + 1):
            old_centers = centers
            if i < nsteps or frame % 3 > 0:
                dist = euclidean_distances(X, centers)
                labels = dist.argmin(1)

            if i < nsteps or frame % 3 > 1:
                centers = np.array([X[labels == j].mean(0)
                                    for j in range(k)])
                nans = np.isnan(centers)
                centers[nans] = old_centers[nans]


        # plot the cluster centers
        fig = plt.figure(figsize=(8,6))

        plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='rainbow');
        plt.scatter(old_centers[:, 0], old_centers[:, 1], marker='s',
                    c="white",
                    s=200)
        plt.scatter(old_centers[:, 0], old_centers[:, 1], marker='s',
                    c=np.arange(k), s=50, cmap='rainbow')

        # plot new centers if third frame
        if frame % 3 == 2:
            for i in range(k):
                plt.annotate('', centers[i], old_centers[i],
                             arrowprops=dict(arrowstyle='->', linewidth=1))
            plt.scatter(centers[:, 0], centers[:, 1], marker='s',
                        c="white",
                        s=200, cmap='rainbow')
            plt.scatter(centers[:, 0], centers[:, 1], marker='s',
                        c=np.arange(k), s=50, cmap='rainbow')

        plt.xlim(-4, 4)
        plt.ylim(-2, 10)

        if frame % 3 == 1:
            plt.text(3.8, 9.5, "1. Reasignacion de etiquetas",
                     ha='right', va='top', size=14)
        elif frame % 3 == 2:
            plt.text(3.8, 9.5, "2. Calculo de centroides",
                     ha='right', va='top', size=14)

    frame_range = [0,20]
    k_range = [2, n_clusters+2]
    return interact(_kmeans_step, k=k_range, frame=frame_range)
