import numpy as np
import matplotlib.pyplot as plt

f = [25.4, 100, 200]
M = 6

f_1 = f[0]
f_2 = f[1]

f_1 = 25.4
f_2 = 100

x = lambda s_1: s_1/f_1-1
y = lambda x: 1/(M*x)
s_2 = lambda y, s_1: f_2*(y+1) + s_1 + (1/f_1-1/s_1)**-1

#--------------------------------------------------------#

s_1s = np.linspace(30, 150, 100)
s_2s = []
for s_1 in s_1s:
    x_ = x(s_1)
    y_ = y(x_)
    s_2s.append(s_2(y_, s_1))

plt.plot(s_1s, s_2s, label='f_1 = 25.4, f_2 = 100')
plt.xlabel('s_1')
plt.ylabel('s_2')
plt.grid()
plt.legend()
plt.show()

