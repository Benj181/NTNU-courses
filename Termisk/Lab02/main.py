import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
# Side_dict = {'Black': 0, 'White': 1, 'Blank': 2, 'Coarse': 3}

xp = np.array([1.0, 1.43, 1.87, 2.34, 2.85, 3.36, 3.88, 4.41, 4.95, 5.48, 6.03, 6.58, 7.14, 7.71, 8.28, 8.86, 9.44, 10.03, 10.63, 11.24, 11.88, 12.46, 13.08])
fp = np.linspace(300, 2500, 23)

alpha = 5.67e-8
T_0 = 273.15 + 21.1
R_0 = (38.7 - 4.7) / 100

df01 = pd.read_csv(f'{sys.path[0]}\\data01.csv')
df02 = pd.read_csv(f'{sys.path[0]}\\data02.csv')

V_s = df02['V_s'].to_numpy()
V = df02['V'].to_numpy()
I = df02['I'].to_numpy()
R = V / I

T = np.interp(R/R_0, xp, fp)
m,b = np.polyfit(np.log10(T), np.log10(V_s), 1)

print(m, b)

# plt.plot(np.log10(T), np.log10(V_s), 'o', label='Experimental Data')
# plt.xlabel('Temperature [K]')
# plt.ylabel('Voltage [V]')
# plt.title('Voltage vs Temperature')
# plt.legend()
# plt.show()




