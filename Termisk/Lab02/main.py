import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
# Side_dict = {'Black': 0, 'White': 1, 'Blank': 2, 'Coarse': 3}


alpha = 5.67e-8
T_0 = 273.15 + 21.1
R_0 = (38.7 - 4.7) / 100

def emmisivity():
    df01 = pd.read_csv(f'{sys.path[0]}\\data01.csv')
    pivot_df = df01.pivot(index='Setting', columns='Side', values='V_s')

    # Calculating the ratio for 'blank', 'white', and 'coarse' divided by 'black'
    pivot_df['blank/black'] = pivot_df['blank'] / pivot_df['black']
    pivot_df['white/black'] = pivot_df['white'] / pivot_df['black']
    pivot_df['coarse/black'] = pivot_df['coarse'] / pivot_df['black']

    # # Display the resulting DataFrame
    # print(pivot_df[['blank/black', 'white/black', 'coarse/black']])
    # mean_ratios = pivot_df[['blank/black', 'white/black', 'coarse/black']].mean()
    # print(mean_ratios)

    std_df = pd.DataFrame({
    'black': [0.05, 0.05, 0.05, 0.05],
    'blank': [0.05, 0.05, 0.05, 0.05],
    'white': [0.05, 0.05, 0.05, 0.05],
    'coarse': [0.05, 0.05, 0.05, 0.05]
        }, index=[5.0, 6.5, 8.0, 10.0])

    # Create an empty DataFrame to store the standard deviations of the ratios
    std_ratio_df = pd.DataFrame(index=pivot_df.index)

    # Calculate standard deviation of the ratios
    for side in ['blank', 'white', 'coarse']:
        std_ratio_df[f'{side}/black'] = (pivot_df[side] / pivot_df['black']) * np.sqrt(
            (std_df[side] / pivot_df[side])**2 + (std_df['black'] / pivot_df['black'])**2
        )

    # Display the resulting DataFrame with standard deviations
    print(f'pivot \n{pivot_df}')
    print('-----------------------------------')
    print(f'std \n{std_ratio_df}')
    print('-----------------------------------')

    def round_to_sig(x, sig=4):
        return np.format_float_positional(x, precision=sig, unique=False, fractional=False, trim='k')

    ratio_columns = ['blank/black', 'white/black', 'coarse/black']

    # Filter pivot_df and std_ratio_df to include only ratio columns
    filtered_pivot_df = pivot_df[ratio_columns]
    filtered_std_ratio_df = std_ratio_df[ratio_columns]

    # Create an empty DataFrame to store the results in "V ± σ" format
    combined_df = pd.DataFrame(index=pivot_df.index)

    # Combine the filtered DataFrames in the format "V ± σ"
    # for col in filtered_pivot_df.columns:
    #     combined_df[col] = filtered_pivot_df[col].astype(str) + " ± " + filtered_std_ratio_df[col].astype(str)

    for col in filtered_pivot_df.columns:
        combined_df[col] = [f"{round((v),4)} ± {round_to_sig(s)}"
                            for v, s in zip(filtered_pivot_df[col].astype(float), filtered_std_ratio_df[col].astype(float))]
    # Display the combined DataFrame
    print(combined_df)



# print('Emmisivity')
# emmisivity()

def Steffan_Boltzmann():
    # Table values to interpolate R/R_0
    xp = np.array([1.0, 1.43, 1.87, 2.34, 2.85, 3.36, 3.88, 4.41, 4.95, 5.48, 6.03, 6.58, 7.14, 7.71, 8.28, 8.86, 9.44, 10.03, 10.63, 11.24, 11.88, 12.46, 13.08])
    fp = np.linspace(300, 2500, 23)

    df02 = pd.read_csv(f'{sys.path[0]}\\data02.csv')
    V_s = df02['V_s'].to_numpy()
    V = df02['V'].to_numpy()
    I = df02['I'].to_numpy()
    R = V / I

    T = np.interp(R/R_0, xp, fp)
    lgT, lgV_s  = np.log10(T), np.log10(V_s)

    coefficients  = np.polyfit(lgT, lgV_s, 1)
    poly_eq = np.poly1d(coefficients)
    V_s_pred = poly_eq(lgT)
    residuals = lgV_s - V_s_pred
    std_dev = np.std(residuals)
    print(f"Coefficients: {coefficients}")
    print(f"Standard Deviation of the residuals: {std_dev}")

    reg_func = lambda x: coefficients[0] * x + coefficients[1]
    reg_T = np.linspace(min(lgT), max(lgT), 100)
    plt.plot(np.log10(T), np.log10(V_s), 'o', label='Experimental Data')
    plt.plot(reg_T, reg_func(reg_T), label='polyfit [{:.2f}x {:.2f}]'.format(coefficients[0], coefficients[1]))

    plt.xlabel('Temperature [K] (log-scale)')
    plt.ylabel('Voltage [V] (log-scale)')
    plt.title('Voltage vs Temperature in log-scale')
    plt.legend()
    plt.show()

print('\nSteffan-Boltzmann')
Steffan_Boltzmann()

