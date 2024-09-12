import numpy as np
import matplotlib.pyplot as plt

theta = np.zeros(100)
omega = np.zeros(100)
theta[0] = 0.5
omega[0] = 1

for i in range(0, 99):
    theta[i + 1] = theta[i] + omega[i] * 0.1
    omega[i + 1] = omega[i] - 9.81/10*np.sin(theta[i]) * 0.1

plt.plot(np.linspace(0, 10, 100), theta)
plt.show()
