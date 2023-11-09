import numpy as np
import matplotlib.pyplot as plt

# Frecvența de eșantionare
fs = 1000  # Hz

# Durata semnalelor
durata = 1  # secunde

# Generează vectorul de timp
t = np.linspace(0, durata, durata * fs, endpoint=False)

# Generează cele trei semnale sinusoidale
f1 = fs / 2
semnal1 = np.sin(2 * np.pi * f1 * t)

f2 = fs / 4
semnal2 = np.sin(2 * np.pi * f2 * t)

f3 = 0  # frecvența zero
semnal3 = np.sin(2 * np.pi * f3 * t)

# Afișează graficele semnalelor
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t, semnal1)
plt.title(f'Semnal sinusoidal 1 - Frecvența: {f1} Hz')

plt.subplot(3, 1, 2)
plt.plot(t, semnal2)
plt.title(f'Semnal sinusoidal 2 - Frecvența: {f2} Hz')

plt.subplot(3, 1, 3)
plt.plot(t, semnal3)
plt.title(f'Semnal sinusoidal 3 - Frecvența: {f3} Hz')

plt.tight_layout()
plt.show()