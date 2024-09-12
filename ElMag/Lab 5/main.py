import numpy as np

def main():
    R = 30.0e-3
    data = np.loadtxt('data.csv', delimiter=',', skiprows=1)
    data = np.transpose(data)
    F = data[2]
    Sigma = F / (4 * np.pi * R)
    data = np.vstack((data, Sigma))
    mean = np.mean(data[3,0:3])
    std = np.std(data[3,0:3])
    print(data)
    print(f'Overflate spenningen ved {round(np.mean(data[1, 0:3]), 2)} C er {round(mean, 3)} +- {round(std, 3)} N/m')

main()
