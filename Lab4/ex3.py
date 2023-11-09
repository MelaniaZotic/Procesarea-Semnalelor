import numpy as np
import matplotlib.pyplot as plt

# Parametrii semnalului
f_original = 5  # frecventa semnalului original in Hz
f_sampling = 10  # frecventa de esantionare in Hz, Nyquist satisfied
t_max = 2       # durata semnalului in secunde

# Calculam perioada de esantionare
t_sampling = 1 / f_sampling

# Generam axa timpului pentru semnalul continuu si pentru esantioane
t_continuous = np.linspace(0, t_max, 1000)  # timp pentru semnalul continuu
t_samples = np.arange(0, t_max, t_sampling)  # momentele de esantionare

# Generam semnalul sinusoidal original
signal_original = np.sin(2 * np.pi * f_original * t_continuous)

# Semnalele de frecvente diferite care vor produce aliere
f_alias1 = f_sampling - f_original  # 5 Hz
f_alias2 = f_sampling + f_original  # 15 Hz

# Generam cele doua semnale care vor cauza aliere
signal_alias1 = np.sin(2 * np.pi * f_alias1 * t_continuous)
signal_alias2 = np.sin(2 * np.pi * f_alias2 * t_continuous)

# Eșantionăm toate cele trei semnale
samples_original = np.sin(2 * np.pi * f_original * t_samples)
samples_alias1 = np.sin(2 * np.pi * f_alias1 * t_samples)
samples_alias2 = np.sin(2 * np.pi * f_alias2 * t_samples)

# Crearea figurii cu subploturi
plt.figure(figsize=(12, 8))

# Semnalul original
plt.subplot(3, 1, 1)
plt.plot(t_continuous, signal_original, label='Semnal Original Continuu')
plt.stem(t_samples, samples_original, 'r', markerfmt='ro', label='Eșantioane Original', basefmt=" ")
plt.title('Semnal Original și Eșantioanele Sale')
plt.legend()

# Primul semnal aliat
plt.subplot(3, 1, 2)
plt.plot(t_continuous, signal_alias1, label='Semnal Aliat 1 Continuu')
plt.stem(t_samples, samples_alias1, 'g', markerfmt='go', label='Eșantioane Aliat 1', basefmt=" ")
plt.title('Primul Semnal Aliat și Eșantioanele Sale')
plt.legend()

# Al doilea semnal aliat
plt.subplot(3, 1, 3)
plt.plot(t_continuous, signal_alias2, label='Semnal Aliat 2 Continuu')
plt.stem(t_samples, samples_alias2, 'm', markerfmt='mo', label='Eșantioane Aliat 2', basefmt=" ")
plt.title('Al Doilea Semnal Aliat și Eșantioanele Sale')
plt.legend()

# Afișare figură
plt.tight_layout()
plt.savefig('fara_aliere.png')
plt.show()