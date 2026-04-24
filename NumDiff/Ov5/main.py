import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve

def make_FTBS_matrix(M, r):
    diagonals = [(1 - r)*np.ones(M), r*np.ones(M-1)]
    offsets = [0, -1]
    A = diags(diagonals, offsets, shape=(M, M), format='csr')
    return A

def solve_FTBS(r, h, k, t_end, g):
    M = round(3 / h)
    Nt = round(t_end / k)

    U = np.zeros(M)
    A = make_FTBS_matrix(M, r)

    b = np.zeros(M)
    U_hist = [U.copy()]
    for n in range(Nt):
        t_n = n * k
        b[0] = r * g(t_n)
        U = A @ U + b
        U_hist.append(U.copy())

    return np.array(U_hist)

def make_lax_wendroff_matrix(M, r):
    diagonals = [(r * (r - 1) / 2)*np.ones(M-1), (1-r**2) * np.ones(M), r * (1 + r) / 2 * np.ones(M-1)]
    offsets = [1, 0, -1]
    A = diags(diagonals, offsets, shape=(M, M), format='csr')
    return A

def solve_lax_wendroff(r, h, k, t_end, g):
    M = round(3 / h)
    Nt = round(t_end / k)

    U = np.zeros(M)
    A = make_lax_wendroff_matrix(M, r)

    b = np.zeros(M)
    U_hist = [U.copy()]
    for n in range(Nt):
        t_n = n * k
        b[0] = r * (1 + r) / 2 * g(t_n)
        U = A @ U + b
        U_hist.append(U.copy())

    return np.array(U_hist)

def solve_wendroff(r, h, k, t_end, g):
    M = round(3 / h)
    Nt = round(t_end / k)
    alpha = (1 - r) / (1 + r)

    U = np.zeros(M)

    L = diags([np.ones(M), alpha * np.ones(M - 1)], [0, -1],
              shape=(M, M), format='csr')
    R = diags([alpha * np.ones(M), np.ones(M - 1)], [0, -1],
              shape=(M, M), format='csr')

    b = np.zeros(M)
    U_hist = [U.copy()]
    for n in range(Nt):
        t_n = n * k
        t_next = (n + 1) * k
        b[0] = g(t_n) - alpha * g(t_next)
        U = spsolve(L, R @ U + b)
        U_hist.append(U.copy())

    return np.array(U_hist)

def g(t):
    return 1

r = 1


a = 1
h = 1/160
k = r * h

t_end = 2

# U_hist = solve_FTBS(r, h, k, t_end, g)
# U_hist = solve_lax_wendroff(r, h, k, t_end, g)
U_hist = solve_wendroff(r, h, k, t_end, g)
x = np.linspace(0, 3, U_hist.shape[1])

fig, ax = plt.subplots()
line, = ax.step(x, U_hist[0], label='Wendroff')
ax.set_xlabel('x')
ax.set_ylabel('U')
ax.set_title('Wendroff Solution as a Moving Wave')
ax.set_xlim(0, 3)
ax.set_ylim(np.min(U_hist) - 0.05, np.max(U_hist) + 0.05)
ax.legend()
ax.grid()

time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

def update(frame):
    line.set_ydata(U_hist[frame])
    time_text.set_text(f't = {frame * k:.2f}')
    return line, time_text

anim = FuncAnimation(fig, update, frames=len(U_hist), interval=1, blit=True)
plt.show()