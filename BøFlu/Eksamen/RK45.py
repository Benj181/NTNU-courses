import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

fun = lambda t, y : [y[1], -9.81/10*np.sin(y[0])]
sol = solve_ivp(fun, [0, 10], [0.5, 1], t_eval=np.linspace(0, 10, 100))
plt.plot(sol.t, sol.y[0])
plt.show()

