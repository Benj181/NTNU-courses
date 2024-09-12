import numpy as np
from matplotlib import pyplot as plt
import math
import pandas as pd
from IPython.display import display

def get_data(filename):
    filename = f'experimentalData\{filename}\Raw Data.csv'
    data = np.loadtxt(filename, delimiter=';', skiprows=1)
    t, x, y, z = data[:, 0], data[:, 1], data[:, 2], data[:, 3]
    return t, x, -y, -z 
 
def main():
    xL, yL, zL, tL = [], [], [], []

    for i in range(1, 6):
        t, x, y, z = get_data(f'Magnetometer0{i}')
        tL.append(t)    
        xL.append(x)
        yL.append(y)
        zL.append(z)
        
    mx = np.mean([np.mean(x) for x in xL])
    my = np.mean([np.mean(y) for y in yL])
    mz = np.mean([np.mean(z) for z in zL])

    stdx = np.mean([np.std(x) for x in xL])
    stdy = np.mean([np.std(y) for y in yL])
    stdz = np.mean([np.std(z) for z in zL])

    sx = np.mean([abs(max(x) - min(x)) for x in xL])
    sy = np.mean([abs(max(y) - min(y)) for y in yL])
    sz = np.mean([abs(max(z) - min(z)) for z in zL])
    
    df = pd.DataFrame({
    "Mean": [mx, my, mz],
    "Std": [stdx, stdy, stdz],
    "Spread": [sx, sy, sz]
    })

    df.index = ['x', 'y', 'z']
    display(df)
    
    dec = np.degrees(math.atan(mx / my))
    inc = np.degrees(math.atan(mz / math.sqrt(mx**2 + my**2)))   
    print(f'The declination is {dec} degrees')
    print(f'The inclination is {inc} degrees')

    # Bare brukt for testing
    # fig, axs = plt.subplots(5, 1, figsize=(10, 10))
    # for i in range(len(tL)):
    #     axs[i].plot(tL[i], xL[i], label=f'Magnetometer0{i}')
    #     axs[i].set_xlabel('Time (s)')
    #     axs[i].set_ylabel('Magnetic field (uT)')
    #     axs[i].set_title('Magnetic field in x')
    # plt.legend()
    # plt.show()

if (__name__ == '__main__'):
    main()
