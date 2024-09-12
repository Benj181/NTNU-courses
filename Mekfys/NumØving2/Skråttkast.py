import numpy as np
import matplotlib.pyplot as plt

g = -9.81
b = 0.3
m = 1

s_0x, s_0y = (0, 300)
v_0, theta = (10, np.pi/4)
v_0x, v_0y = (v_0 * np.cos(theta), v_0 * np.sin(theta))
n = 1000
t_start = 0
t_end = 100
t = np.zeros(n)
dt = (t_end - t_start) / n

x = np.zeros(n)
x[0] = s_0x
y = np.zeros(n)
y[0] = s_0y
v_x = np.zeros(n)
v_x[0] = v_0x
v_y = np.zeros(n)
v_y[0] = v_0y

def a_x(v, b, m):
    return - (b * v) / m

def a_y(v, b, m, g):
    return (m * g - b * v) / m

for i in range(1, n):
    v_x[i] = v_x[i - 1] + a_x(v_x[i - 1], b, m) * dt
    v_y[i] = v_y[i - 1] + a_y(v_y[i - 1], b, m, g) * dt
    x[i] = x[i - 1] + v_x[i - 1] * dt
    y[i] = y[i - 1] + v_y[i - 1] * dt

    if y[i] < 0:
        stop = i
        break
    else:
        stop = 0

if stop:
    print(stop*dt)
    plt.plot(x[:stop], y[:stop])

else:
    plt.plot(x, y)
plt.grid()
plt.show()