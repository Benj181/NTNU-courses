import numpy as np
import matplotlib.pyplot as plt

def fresnel_coefficients(theta_i, n1, n2, polarization):
    """
    Calculate the amplitude reflection coefficients for TE and TM polarized light.
    """
    theta_i_rad = np.radians(theta_i)
    theta_t_rad = np.arcsin(n1 * np.sin(theta_i_rad) / n2)  # Snell's law
    
    cos_theta_i = np.cos(theta_i_rad)
    cos_theta_t = np.cos(theta_t_rad)
    
    if polarization == 'TE':
        r = (n1 * cos_theta_i - n2 * cos_theta_t) / (n1 * cos_theta_i + n2 * cos_theta_t)
    elif polarization == 'TM':
        r = (n2 * cos_theta_i - n1 * cos_theta_t) / (n2 * cos_theta_i + n1 * cos_theta_t)
    else:
        raise ValueError("Polarization must be 'TE' or 'TM'")
    
    return r

def brewster_angle(n1, n2):
    """Calculate Brewster's angle in degrees."""
    return np.degrees(np.arctan(n2 / n1))

def critical_angle(n1, n2):
    """Calculate the critical angle for total internal reflection in degrees."""
    if n1 > n2:
        return np.degrees(np.arcsin(n2 / n1))
    return None  # No TIR if n1 < n2

# Constants
n_air = 1.000
n_water = 1.334
n_water = 1.5195

theta_i_ext = np.linspace(0, 90, 500)  # Incident angles (0 to 90 degrees)
theta_i_int = np.linspace(0, 90, 500)  # Incident angles (0 to 90 degrees)

# Compute reflection coefficients
r_TE_ext = fresnel_coefficients(theta_i_ext, n_air, n_water, 'TE')
r_TM_ext = fresnel_coefficients(theta_i_ext, n_air, n_water, 'TM')
r_TE_int = fresnel_coefficients(theta_i_int, n_water, n_air, 'TE')
r_TM_int = fresnel_coefficients(theta_i_int, n_water, n_air, 'TM')

# Compute intensities
R_TE_ext = r_TE_ext**2
T_TE_ext = 1 - R_TE_ext
R_TM_ext = r_TM_ext**2
T_TM_ext = 1 - R_TM_ext

R_TE_int = r_TE_int**2
T_TE_int = 1 - R_TE_int
R_TM_int = r_TM_int**2
T_TM_int = 1 - R_TM_int

# Compute Brewster angles
brewster_ext = brewster_angle(n_air, n_water)
brewster_int = brewster_angle(n_water, n_air)

# Compute Critical angle
critical_int = critical_angle(n_water, n_air)

# Plot results
plt.figure(figsize=(12, 10))

# External reflection coefficients
plt.subplot(3, 2, 1)
plt.plot(theta_i_ext, r_TE_ext, label='r TE')
plt.plot(theta_i_ext, r_TM_ext, label='r TM')
plt.axvline(brewster_ext, color='gray', linestyle='--', label=f'Brewster: {brewster_ext:.2f}°')
plt.xlabel('Incident Angle (degrees)')
plt.ylabel('Reflection Coefficient')
plt.title('External Reflection Coefficients (Air to Water)')
plt.legend()
plt.grid()

# Internal reflection coefficients
plt.subplot(3, 2, 2)
plt.plot(theta_i_int, r_TE_int, label='r TE')
plt.plot(theta_i_int, r_TM_int, label='r TM')
if critical_int:
    plt.axvline(critical_int, color='red', linestyle='--', label=f'Critical Angle: {critical_int:.2f}°')
plt.xlabel('Incident Angle (degrees)')
plt.ylabel('Reflection Coefficient')
plt.title('Internal Reflection Coefficients (Water to Air)')
plt.legend()
plt.grid()

# External reflection intensities
plt.subplot(3, 2, 3)
plt.plot(theta_i_ext, R_TE_ext, label='R TE')
plt.plot(theta_i_ext, R_TM_ext, label='R TM')
plt.xlabel('Incident Angle (degrees)')
plt.ylabel('Reflection Intensity')
plt.title('External Reflection Intensities (Air to Water)')
plt.legend()
plt.grid()

plt.subplot(3, 2, 4)
plt.plot(theta_i_ext, T_TE_ext, label='T TE')
plt.plot(theta_i_ext, T_TM_ext, label='T TM')
plt.xlabel('Incident Angle (degrees)')
plt.ylabel('Transmission Intensity')
plt.title('External Transmission Intensities (Air to Water)')
plt.legend()
plt.grid()

# Internal reflection intensities
plt.subplot(3, 2, 5)
plt.plot(theta_i_int, R_TE_int, label='R TE')
plt.plot(theta_i_int, R_TM_int, label='R TM')
if critical_int:
    plt.axvline(critical_int, color='red', linestyle='--', label=f'Critical Angle: {critical_int:.2f}°')
plt.xlabel('Incident Angle (degrees)')
plt.ylabel('Reflection Intensity')
plt.title('Internal Reflection Intensities (Water to Air)')
plt.legend()
plt.grid()

plt.subplot(3, 2, 6)
plt.plot(theta_i_int, T_TE_int, label='T TE')
plt.plot(theta_i_int, T_TM_int, label='T TM')
plt.xlabel('Incident Angle (degrees)')
plt.ylabel('Transmission Intensity')
plt.title('Internal Transmission Intensities (Water to Air)')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

# Print angles
print(f"Brewster angle (Air to Water): {brewster_ext:.2f} degrees")
print(f"Brewster angle (Water to Air): {brewster_int:.2f} degrees")
if critical_int:
    print(f"Critical angle for total internal reflection: {critical_int:.2f} degrees")

