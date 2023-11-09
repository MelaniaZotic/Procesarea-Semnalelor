import numpy as np
import matplotlib.pyplot as plt

# Frecvența de eșantionare
fs = 1000  # Hz

# Durata semnalului
durata = 1  # secunde

# Generează vectorul de timp
t = np.linspace(0, durata, durata * fs, endpoint=False)

# Generează semnalul sinusoidal
frecventa = 50  # Hz
semnal_original = np.sin(2 * np.pi * frecventa * t)

# Decimează semnalul la 1/4 din frecvența inițială (păstrând doar al 4-lea element)
semnal_decimat_1 = semnal_original[::4]

# Decimează semnalul la 1/4 din frecvența inițială, începând de la al doilea element
semnal_decimat_2 = semnal_original[1::4]

# Afișează graficele semnalelor
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(t, semnal_original)
plt.title(f'Semnal Original - Frecvența de Eșantionare: {fs} Hz')

plt.subplot(3, 1, 2)
plt.plot(np.arange(0, len(semnal_original), 4), semnal_decimat_1, 'ro-', label='Decimat la 1/4')
plt.title('Decimare de la Început')

plt.subplot(3, 1, 3)
plt.plot(np.arange(1, len(semnal_original), 4), semnal_decimat_2, 'go-', label='Decimat la 1/4')
plt.title('Decimare de la Al Doilea Element')

plt.tight_layout()
plt.show()