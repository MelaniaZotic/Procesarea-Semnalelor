import numpy as np
import matplotlib.pyplot as plt

# Creează un vector de timp
t = np.linspace(0, 1, 800)

# Generez semnalul sinusoidal
signal_sin = np.sin(2 * np.pi * 5 * t)

# Genereaza semnalul sawtooth
signal_sawtooth = 0.7 * (1 - np.mod(2 * t, 2))

# suma semnalelor:
signal_sum = signal_sin + signal_sawtooth


# Calculează suma semnalelor
signal_sum = signal_sin + signal_sawtooth

# Afișează graficele în subploturi
plt.figure(figsize=(10, 6))

# Subplot pentru semnalul sinusoidal
plt.subplot(3, 1, 1)
plt.plot(t, signal_sin)
plt.title('Semnal Sinusoidal')

# Subplot pentru semnalul în formă de dinte de feră
plt.subplot(3, 1, 2)
plt.plot(t, signal_sawtooth)
plt.title('Semnal Sawtooth')

# Subplot pentru suma semnalelor
plt.subplot(3, 1, 3)
plt.plot(t, signal_sum)
plt.title('Suma Semnalelor')

# Afișează graficele
plt.tight_layout()
plt.show()