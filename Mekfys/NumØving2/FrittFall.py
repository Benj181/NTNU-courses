"""Code for obtaining the velocity as a function of time for a ball in free fall using Euler's method.
"""

import numpy as np
import matplotlib.pyplot as plt

g = -9.81  # Gravitational acceleration m/s^2 
init_vel = 10  # Initial velocity m/s

time_start = 0
time_stop = 10
num_steps = 11  # Number of steps from time_start to time_stop
delta_t = 1  # Time discretization

times = np.linspace(time_start, time_stop, num_steps)  # array of times to evaluate from time_start to time_stop
vel_arr = np.zeros(len(times))  # Initialization of array for velocities
vel_arr[0] = init_vel  # v[0] = v(t = 0) = init_vel

for i, vel in enumerate(vel_arr):
    '''
    Loop to iteratively calcutale the velocity of a falling object
    '''
    if i:
        vel_arr[i] = vel_arr[i - 1] - 9.81 * delta_t

plt.plot(times, vel_arr) # plots the function, v

plt.title('Velocity of falling object') # gives the plot a title
plt.ylabel('Velocity [m/s]') # puts a label on the y-axis
plt.xlabel('Time [s]') # puts a label on the x-axis
plt.grid() # shoes a grid in the plot
plt.show() # shoes the plot

