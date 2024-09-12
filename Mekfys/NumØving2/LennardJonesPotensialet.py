import matplotlib.pyplot as plt
import numpy as np

def LJP(epsilon, sigma, r):
    ''' 
    Lennard Jones Potential
    Returns the potential energy of the bond interaction 
    between two atoms or free molecules based 
    on the distance, r, between them

    epsilon: is the depth of the potential well 
    (usually referred to as 'dispersion energy')

    sigma: is the distance at which the particle-particle
    potential energy V is zero (often referred to as 'size of the particle')
    '''
    return epsilon*((sigma/r) ** 12 - 2*(sigma/r) ** 6)

epsilon = 6
sigma = 5
n = 1000 # number of datapoints
r = np.linspace(4, 9, n) # array with different values for the radius
V = np.array([LJP(epsilon, sigma, x) for x in r])

plt.plot(r, np.zeros(n), '--') # plots equilibrium
plt.plot(r,V) # plots V as a function of r
plt.plot([r[np.where(V == min(V))[0]]],
          [min(V)], 
          marker="o", markersize=5) # plots the depth of the potential well 


plt.ylabel('Potential, V')
plt.xlabel('Distance, r')
plt.grid()
plt.savefig('LennardPotential')
plt.show()