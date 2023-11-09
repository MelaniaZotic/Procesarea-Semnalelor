import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write, read

# a
f = 100  # frecventa semnalului
n_f = 10000  # numarul de esantioane
t = n_f / f

timp = np.linspace(0, t, n_f, endpoint=False)  # Vector de timp
s = np.sin(2 * np.pi * f * timp)

plt.plot(timp, s)
plt.title('Punctul a)')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.grid(True)
# plt.show()


# b
frecventa = 500  # Frecventa semnalului în Hz
durata = 3  # Durata semnalului în secunde
frecventa_esantionare = 1500

# Generarea timpului și a semnalului
timp = np.arange(0, durata, 1 / frecventa_esantionare)  # Vector de timp
semnal = np.sin(2 * np.pi * frecventa * timp)  # Semnalul sinusoidal

# Afisarea grafică
plt.plot(timp, semnal)
plt.title('Semnal sinusoidal de 800 Hz')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.grid(True)
# plt.show()

# c

fr = 1000
d = 1
fr_esan = 1000

t = np.arange(0, d, 1 / fr_esan)
semnal_s = np.mod(t, 1 / fr) * fr

plt.plot(t, semnal_s)
plt.title('Semnal sawtooth de 240 Hz')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.grid(True)
# plt.show()


# d
frecv = 2000
durata_s = 1
frecv_es = 40000

timp_square = np.arange(0, durata_s, 1 / frecv_es)
semnal_square = np.sign(np.sin(2 * np.pi * frecv_es * timp_square))

plt.plot(timp_square, semnal_square, color='red')
plt.title('Semnal square de 300 Hz')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.grid(True)
# plt.show()


# semnalul s
sd.play(s, samplerate=n_f)
sd.wait()  # Așteaptă până la sfârșitul redării

# semnalul sinusoidal
sd.play(semnal, samplerate=frecventa_esantionare)
sd.wait()

# semnalul sawtooth
sd.play(semnal_s, samplerate=fr_esan)
sd.wait()

# semnalul square
sd.play(semnal_square, samplerate=frecv_es)
# Funcția sd.wait() este folosită pentru a aștepta finalizarea redării semnalului înainte de a trece la următorul.
sd.wait()

filename = "semnal_sinusoidal.wav"
write(filename, n_f, (semnal_s * 32767).astype(np.int16))

# Citirea fișierului salvat și verificarea
rate, data = read(filename)
plt.figure()
plt.plot(data)
plt.title('Semnalul citit din fișierul .wav')
plt.xlabel('Eșantioane')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.show()
