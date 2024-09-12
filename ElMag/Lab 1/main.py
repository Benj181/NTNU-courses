import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

N = 330 # [] antall viklinger
I0 = 1.0 # [A] strøm
mu_0 = 4.0*np.pi*1e-7 # [H/m] permeabilitet i tomt rom
R = 0.07 # [m] radius
 
def B_func(xe, Be, ftype, a):
    prefaktor = N*mu_0*I0/(2*R)
    x0 = xe[np.argmax(Be)]
    xe = x0 - xe
    xb = np.linspace(xe[0], xe[-1], 1000)
    if ftype == 'kortspole':
        Bb = prefaktor*(1 + (xb/R)**2)**(-1.5)
    elif ftype == 'helmspole':
        Bb = prefaktor*( (1 + (xb - a / 2)**2/R**2)**(-1.5) + (1 + (xb + a / 2)**2/R**2)**(-1.5))
    elif ftype == 'anti_helmspole':
        Bb = prefaktor*( (1 + (xb - a / 2)**2/R**2)**(-1.5) - (1 + (xb + a / 2)**2/R**2)**(-1.5))
    return xe, xb, Bb

def save_data(x, Bb, Be, filename):
    Err_func = lambda Bb, Be: np.abs(2 * (Be - Bb) / (Bb + Be)) * 100
    Er = Err_func(Bb, Be)
    np.savetxt(filename, np.column_stack([x, Bb, Be, Er]), delimiter=',', header='x, Bb, Be', comments='')

def get_data(filename):
    df = pd.read_csv(filename, delimiter=';')
    heads = df.head()
    data = df.to_numpy()
    data = np.transpose(data)
    xarr, Barr = [], []

    for i in range(0, int(len(data)/2), 2):
        df = pd.DataFrame(np.column_stack(data[i:i+2]), columns=['x', 'B'])
        df = df.dropna(subset=['x'])
        df = df.dropna(subset=['B'])
        
        temp = df.to_numpy()
        temp = np.transpose(temp)
        for i in range(2):
            for j in range(len(temp[i])):
                temp[i][j] = temp[i][j].replace(',', '.')
            temp[i] = np.asarray(temp[i], dtype='float')
        xarr.append(temp[0][:-1])
        Barr.append(temp[1][:-1])  

    return xarr, Barr, heads
 
def main():
    xarr, Barr, heads = get_data('dataset.csv') # henter data fra dataset.csv
    xe = xarr[0]
    Be = Barr[0]
    xe, xb, Bb = B_func(xe, Be, 'anti_helmspole', R)

    # plt.plot(xb, Bb, label='Beregnet')
    for i in range(len(xarr)):
        plt.plot(xarr[i], Barr[i], label=f'{heads.columns[i*2 - 1]}')
        
    # plt.errorbar(xe, Be, yerr=abs(Be - Bb), fmt='r.', label='Måledata')

    plt.xlabel('Avstand fra senter av spolen (m)')
    plt.ylabel('Magnetfelt (Gauss)')
    plt.legend()
    plt.show()


if (__name__ == '__main__'):
    main()
