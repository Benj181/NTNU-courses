import numpy as np
import matplotlib.pyplot as plt
from CrankNicolson import *
import os
import sys
 
def data(filename):
    x = []
    t = []
    with open(os.path.join(sys.path[0], filename), 'r') as file:
        for line in file:
            t_, x_, _ = line.split()
            t.append(float(t_))
            x.append(float(x_))
    return np.array(t), np.array(x)

font = {'family' : 'monospace',
        'size'   : 20}

plt.rc('font', **font)

g = 9.81
R = 0.47
size = (10, 5)
'''
M1
'''
TimeArrM1, xArrM1 = data('M1.txt')      
delta_1 = 5e-4
beta_1 = 7e-2
phiR_1 = 2e-4

delta_2 = 7e-3
beta_2 = 9e-2
phiR_2 = 6.5e-4

r_1 = 0.06/2
c_1 = 0.5
w0_1 = np.sqrt(g/(R - r_1) * 1/(1 + c_1)) - 0.05
l = R - r_1

Correction1 = 0.559
PhiArrM1 = np.arcsin((xArrM1 - Correction1)/l)
DeltaTimeArrM1 = TimeArrM1[-1]/len(TimeArrM1)
StartTimeM1 = TimeArrM1[0]
EndTimeM1 = TimeArrM1[-1]
StartAngleM1 = max(PhiArrM1)

fig, ax = plt.subplots(figsize=size)
t_CN_1, phi_CN_1, _ = ODE_solver_lab_3b(DeltaTimeArrM1, StartTimeM1, EndTimeM1, StartAngleM1, 0, w0_1, 1, phiR_1, delta_1, beta_1, )
ax.plot(t_CN_1, phi_CN_1, 'b', lw=1, label='Numerisk')
ax.plot(TimeArrM1, PhiArrM1, 'r', lw=1, label='Eksperimentell')
ax.set_ylabel('$\\phi$ [rad]')
ax.set_xlabel('t [s]')
ax.grid()
ax.legend(loc='upper right')
plt.savefig('m1.pdf', bbox_inches="tight")

'''
M2
'''

TimeArrM2, xArrM2 = data('M2.txt')  

c_2 = 0.66
r_2 = 0.067/2
w0_2 = np.sqrt(g/(R - r_1) * 1/(1 + c_2)) + 0.05
l = R - r_1

Correction2 = 0.113
PhiArrM2 = np.arcsin((xArrM2 - Correction2)/l)
DeltaTimeArrM2 = TimeArrM2[-1]/len(TimeArrM2)
StartTimeM2 = TimeArrM2[0]
EndTimeM2 = TimeArrM2[-1]  
StartAngleM2 = max(PhiArrM2)

# fig, ax = plt.subplots(figsize=size)
# t_CN_2, phi_CN_2, _ = ODE_solver_lab_3b(DeltaTimeArrM2, StartTimeM2, EndTimeM2, StartAngleM2, 0, w0_2, 1, phiR_2, delta_2, beta_2)
# ax.plot(t_CN_2, phi_CN_2,'b', lw=1, label='Numerisk')
# ax.plot(TimeArrM2, PhiArrM2, 'r', lw=1, label='Eksperimentell')
# ax.set_ylabel('$\\phi$ [rad]')
# ax.set_xlabel('t [s]')
# ax.grid()
# ax.legend(loc='upper right')
# plt.savefig('m2.pdf', bbox_inches="tight")
plt.show()