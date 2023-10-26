import numpy as np
import matplotlib.pyplot as plt

# Definirea parametrilor:
amplitudine = 1
frecventa = 5
t = np.arange(0, 1, 0.01)

faze = [np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 6]
semnale = [amplitudine * np.sin(2 * np.pi * frecventa * t + faza) for faza in faze]

# Afisarea semnalelor
plt.figure(figsize=(10, 6))
for signal, faza in zip(semnale, faze):
    plt.plot(t, signal, label=f'Faza = {faza}')
plt.legend()
plt.title('Semnale sinusoidale cu faze diferite')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.show()


# am creat o functie pentru a calcula gamma dupa formula din enunt

def calc_gamma(s, z, SNR):
    semnal_patrat = np.linalg.norm(s) ** 2
    zgomot_patrat = np.linalg.norm(z) ** 2
    g = np.sqrt(semnal_patrat / (SNR * zgomot_patrat))
    return g

# x este primul semnal
x = semnale[0]
# zgomotul
z = np.random.randn(len(t))
SNRs = [0.1, 1, 10, 100]

plt.figure(figsize=(12, 8))
for snr in SNRs:
    gamma = calc_gamma(x, z, snr)
    zgomot_semnal = x + gamma * z
    plt.plot(t, zgomot_semnal, label=f'SNR = {snr}')

plt.legend()
plt.title('Semnalul cu faza pi/2 avand zgomot adaugat pentru diferite valori de SNR')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.show()
