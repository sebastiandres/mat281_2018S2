import numpy as np
from numpy.linalg import norm
def lms_regression(X, Y, theta, tol=1E-6):
    converged = False
    alpha = 0.01/len(Y)
    while not converged:
	gradient = 0.
	for xiT, yi in zip(X,Y):
            hi = np.dot(theta, xiT)
            gradient += (hi - yi)*xiT.T
        new_theta = theta - alpha * gradient
	converged = norm(theta-new_theta) < tol * norm(theta) 
	theta = new_theta
    return theta

if __name__=="__main__":
    m = 20
    t = np.linspace(0,1,m)
    x = 2 + 2*t
    y = 300 + 100*t

    X = np.array([np.ones(m), x]).T
    Y = y.reshape(m,1)

    theta_0 = np.array([[0.0,0.0]])
    theta =  lms_regression(X, Y, theta_0)
    print theta
