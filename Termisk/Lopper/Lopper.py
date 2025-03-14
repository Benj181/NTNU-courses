import itertools
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import random as rd

def generate_data(N, tol=None):
    lopper = np.zeros(N)
    N_B = np.array([])
    n = 0
    while True:
        n += 1
        i = rd.randint(0, N-1)
        lopper[i] = 1 if lopper[i] == 0 else 0
        N_B = np.append(N_B, np.sum(lopper))

        if tol is not None:
            if abs(np.mean(N_B) - N/2) < tol:
                break
        else:
            if n > 100:
                break

    N_A = N - N_B
    return N_A

for N, tol in [(6, None), (100, 5), (1000, 50), (10000, 500)]:
    N_A = generate_data(N, tol)
    f = lambda t: N/2*(1 + np.exp(-2*t/N))
    t_ = np.linspace(0, len(N_A), 10000)
    plt.plot(t_, f(t_), label='Analytical')
    plt.plot(N_A, label=f'Simulation(N={N})')
    plt.xlabel('Time')
    plt.ylabel('Number of lopper in the A state')
    plt.legend()
    plt.show()


def data_gen(): # Generator function for the animation
    for cnt in itertools.count():
        t = cnt
        yield t, N_A[cnt]

def init(): # Initialize the plot
    ax.set_ylim(0, N)
    ax.set_xlim(0, 1)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

# Set up the figure, the axis, and the plot element we want to animate
fig, ax = plt.subplots()
ax.set_xlabel('Time')
ax.set_ylabel('Number of lopper in the A state')
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []

# Generate the data
N = 100
tol = 5
lopper = np.zeros(N) # Every element is a loppe
N_B = np.array([]) # Number of lopper in the B state every iteration
while True:
    i = rd.randint(0, N-1)
    lopper[i] = 1 if lopper[i] == 0 else 0
    N_B = np.append(N_B, np.sum(lopper))
    if abs(np.mean(N_B) - N/2) < tol:
        break

# Analytical solution
f = lambda t: N/2*(1 + np.exp(-2*t/N))
t_ = np.linspace(0, len(N_B), 10000)
plt.plot(t_, f(t_))
N_A = N - N_B

def run(data): # Update the plot
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)
    return line,

# Animation
ani = animation.FuncAnimation(fig, run, data_gen, interval=5, init_func=init,
                              save_count=100, blit=True)
plt.show()
