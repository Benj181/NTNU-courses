import numpy as np

R = 0.31/2 # Radius of the spool
n = 130 # Number of turns
m_0 = 4 * np.pi * 1e-7 # Permeability of free space

f = lambda I, r, U: 2 * U / (r * m_0 * (4/5)**(3/2) * (n * I) / R)**2

U = [102, 144, 82]
r = [0.114 / 2, 0.094 / 2, 0.103 / 2]
I = [0.856, 1.131, 0.771]

print('Forholdet mellom elektron ladningen og elektron massen:')
print('> 1.76 e11\n')
print('Mens de målte størrelsene var:')
for i in range(3):
    e_m = f(I[i], r[i], U[i])
    print('> {:.2E}'.format(e_m))

# Error analysis
def error(I, r, U):
    dI = 10e-3
    dr = 5e-3
    dU = 1

    df_dI = lambda I, r, U: -4 * U / ((r * m_0 * (4/5)**(3/2) * n / R)**2 * I **3)
    df_dd = lambda I, r, U: -4 * U / ((r * m_0 * (4/5)**(3/2) * n / R)**2 * r **3)
    df_dU = lambda I, r, U: 2 / (r * m_0 * (4/5)**(3/2) * (n * I) / R)**2

    de_m = np.sqrt(df_dI(I, r, U)**2 * dI**2 + df_dd(I, r, U)**2 * dr**2 + df_dU(I, r, U)**2 * dU**2)
    return de_m

print('\nFeilen i e_m er:')
for i in range(3):
    de_m = error(I[i], r[i], U[i])
    print('> {:.2E}'.format(de_m))


print((4/5)**(3/2))