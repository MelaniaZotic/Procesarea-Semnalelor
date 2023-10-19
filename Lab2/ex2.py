import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile
import scipy.signal

# Definirea parametrilor:
amplitudine = 1
frecventa = 5
t = np.arange(0, 1, 0.01)

faze = [np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 6]
semnale = [amplitudine * np.sin(2 * np.pi * frecventa * t + faza) for faza in faze]

plt.figure(figsize=(10, 6))
for semnal, faza in zip(semnale, faze):
    plt.plot(t, semnal, label=f'Faza = {faza} rad')
plt.title('Semnale sinusoidale cu faze diferite')
plt.xlabel('Timp')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.show()


def calc_gamma(s, z, SNR):
    semnal_patrat = np.linalg.norm(s) ** 2
    zgomot_patrat = np.linalg.norm(z) ** 2
    g = np.sqrt(semnal_patrat / (SNR * zgomot_patrat))

    return g


zgomot_Gaussian = np.random.normal(1, len(semnale))
snrs = [0.1, 1, 10, 100]

for snr in snrs:
    gamma = calc_gamma(semnale[0], zgomot_Gaussian, snr)
    zgomot_semnal = semnale[0] + gamma * zgomot_Gaussian
    plt.plot(t, zgomot_semnal, label=f'SNR = {snr}')
plt.legend()
plt.title('Semnal sinusoidal cu zgomot Gaussian pentru diferite SNRs')
plt.xlabel('Timp')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.show()

