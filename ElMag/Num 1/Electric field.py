import matplotlib.pyplot as plt 
import numpy as np

def f(V, n):
    Ex, Ey = [], []
    
    for i in range(0, n):
        Ex.append(-np.gradient(V[i]))

    for i in range(0, n):
        trsp = np.transpose(V)[i]
        Ey.append(-np.gradient(trsp))

    return np.array(Ex), np.transpose(np.array(Ey))

n = 30
xv, yv = np.meshgrid(np.linspace(-1, 1, n), np.linspace(-1, 1, n))     
V = 1 / np.sqrt(xv ** 2 + yv ** 2)
Ex, Ey = f(V, n)

fig, ax = plt.subplots()
qq = plt.quiver(xv, yv, np.clip(Ex, -1, 1), np.clip(Ey, -1, 1), np.sqrt(xv**2 + yv**2), cmap=plt.cm.plasma)
ax.set_title('Electrical field')
plt.show()