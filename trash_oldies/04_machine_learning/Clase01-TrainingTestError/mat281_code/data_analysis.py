import numpy as np
from matplotlib import pyplot as plt

# Define error function
def error(vector_e):
  return abs(vector_e).mean()

# Load the data
N = 200
data = np.loadtxt("dataN%d.txt"%N)
sorted = True
s = "sorted" if sorted else ""
nmax = 71

# Some properties
color_t = "b"
color_p = "g"

# Sort or keep it unsorted
if sorted:
  data = data[np.argsort(data[:,0])]

# Split into training and prediction data
t = int(N*.7)
x_t = data[:t,0]
x_p = data[t:,0]
y_t = data[:t,1]
y_p = data[t:,1]

# Some helper variables for nicer plotting
x = np.linspace(data[:,0].min(), data[:,0].max(), 1000)

# Fit best several models and record training error and prediction error
n_range = range(1, nmax)
error_t = []
error_p = []
for n in n_range:
  fit_n = np.polyfit(x_t, y_t, n) # Obtains the best fitted polynomial of degree n
  pol_n = np.poly1d(fit_n) # Creates the polynomial with coefficients as in fit n
  plt.plot(x_t, y_t, 's'+color_t, alpha=0.5, label="Datos de Entrenamiento de Modelo")
  if t<N:
    plt.plot(x_p, y_p, 'o'+color_p, alpha=0.5, label="Datos para Testeo de Modelo")
  plt.plot(x, 5*np.cos(.25*np.pi*x), 'k-', lw=2.0, label="Relacion determinista")
  plt.plot(x, pol_n(x), 'r-', lw=2.0, label="Polinomio de grado %d"%n)
  plt.xlim([-2.5,2.5])
  plt.ylim([-5,10])
  plt.legend(numpoints = 1, loc="lower center")
  plt.savefig("images/data%sN%dpol%02d.png"%(s,N,n))
  plt.close()
  error_t.append( error(y_t - pol_n(x_t)) )
  error_p.append( error(y_p - pol_n(x_p)) )

# Plot the errors
plt.loglog(n_range, error_t, "-s"+color_t, lw=2.0, label="Training error")
if t<N:
  plt.loglog(n_range, error_p, "-o"+color_p, lw=2.0, label="Prediction error")
plt.legend(numpoints= 1)
plt.xlabel("Grado del polinomio")
plt.ylabel("Error")
plt.savefig("images/data%s_trainpred.png"%s)
plt.close()

# Save the error
data = np.array([ np.array(error_t), np.array(error_p)]).T
#print data
np.savetxt("images/data%serror_trainpred.txt"%s, data)
