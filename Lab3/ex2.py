import matplotlib.pyplot as plt
import numpy as np

# semnal sinusoidal cu o frecventa de 1800Hz
def semnal_sin(t):
    return np.sin(2 * 1800 * np.pi * t)


# Figura 1
# generăm un vector n cu valori cuprinse între 0 și 1, cu 360 de puncte
n = np.linspace(0, 1, 360)
y = semnal_sin(n) * np.exp(-2j * np.pi * n)

plt.plot(n, semnal_sin(n))
plt.show()
plt.plot(y.real, y.imag)
plt.show()

# Figura 2
# Acest cod creează un set de 4 grafice care arată cum semnalul sinusoidal este afectat atunci când este multiplicat
# cu exponențiale complexe având diferite valori ale frecvenței unghiulare w (10, 100, 700, 1800).
fig, axs = plt.subplots(2, 2)
fig.tight_layout(pad=2.0)

z = semnal_sin(n) * np.exp(-2j * np.pi * n * 10)
axs[0, 0].set_title("w=10")
axs[0, 0].plot(z.real, z.imag)
z = semnal_sin(n) * np.exp(-2j * np.pi * n * 100)
axs[0, 1].set_title("w=100")
axs[0, 1].plot(z.real, z.imag)
z = semnal_sin(n) * np.exp(-2j * np.pi * n * 700)
axs[1, 0].set_title("w=700")
axs[1, 0].plot(z.real, z.imag)
z = semnal_sin(n) * np.exp(-2j * np.pi * n * 1800)
axs[1, 1].set_title("w=1800")
axs[1, 1].plot(z.real, z.imag)
plt.show()
