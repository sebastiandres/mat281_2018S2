import numpy as np
from scipy import random
from matplotlib import pyplot as plt

# Parameters
N = 200
A = 5
E = 1.0
L = 2.0
myseed = 42

# Initialize the random with seed
random.seed(myseed)

# Hidden Model
x = np.linspace(-L, L, N)
y1 = A * np.cos(0.5*np.pi*x/L)
y2 = E * random.normal(size=N)

# Show
plt.plot(x, y1+y2, 'bs', alpha=0.5, label="Medicion")
plt.plot(x, y1,    'k-', lw=2.0, label="Relacion determinista")
plt.xlim([-2.5,2.5])
plt.ylim([-5,10])
plt.xlabel("x []")
plt.ylabel("y []")
plt.legend(numpoints=1, loc="lower center")
#plt.savefig("images/dataN%d.png"%N)
plt.show()

# Shuffle the data
data = np.array([x,y1+y2]).T
data = random.permutation(data)

# Save
np.savetxt("../data/data.txt", data)
