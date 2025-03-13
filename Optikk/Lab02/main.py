import numpy as np
import matplotlib.pyplot as plt

M = 6
f_1 = 100
f_2 = 100


def calc(s_1):
    x = s_1 / f_1 - 1
    y = 1 / (M * x)
    s_o2 = f_2*(1 + y)
    s_2 = s_o2 + s_1 + (1/f_1-1/s_1)**-1
    s_i1 = (1/f_1-1/s_1)**-1
    s_i2 = (1/f_2-1/s_o2)**-1
    l = s_2 + s_i2
    return M, s_2, s_i1, s_o2, s_i2, l

n = 1000
ls = np.zeros(n)
s_1s = np.linspace(110, 300, n)

for i, s_1 in enumerate(s_1s):
    M_, s_2, s_i1, s_o2, s_i2, l = calc(s_1)
    ls[i] = l  

print(f'Minimum system length: {ls.min()}')
s_1 = 150
print('s_1:', s_1)
M_, s_2, s_i1, s_o2, s_i2, l = calc(150)
print('s_i1:', s_i1)
print('s_o2:', s_o2)
print('s_i2:', s_i2)
print('Position of lense 1:', s_1)
print('Position of lense 2:', s_2)
print('Length of system', l)
print('M:', M_)


for i, s_1 in enumerate(s_1s):
    M_, s_2, s_i1, s_o2, s_i2, l = calc(s_1)
    plt.plot(s_1, l, 'ro', markersize=1)

plt.xlabel('s_1')
plt.ylabel('l')
plt.show()


