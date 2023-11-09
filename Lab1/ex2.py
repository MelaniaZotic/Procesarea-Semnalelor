import matplotlib.pyplot as plt
import numpy as np

#a
f = 400 #frecventa semnalului
n_f = 16000 #numarul de esantioane
t = n_f/f

timp = np.linspace(0, t, n_f, endpoint=False)  # Vector de timp
s = np.sin(2*np.pi * f * timp)

plt.plot(timp, s)
plt.title('Punctul a)')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.grid(True)
#plt.show()


#b
frecventa = 800  # Frecventa semnalului în Hz
durata = 3  # Durata semnalului în secunde
frecventa_esantionare = 1600

# Generarea timpului și a semnalului
timp = np.arange(0, durata, 1/frecventa_esantionare)  # Vector de timp
semnal = np.sin(2 * np.pi * frecventa * timp)  # Semnalul sinusoidal

# Afisarea grafică
plt.plot(timp, semnal)
plt.title('Semnal sinusoidal de 800 Hz')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.grid(True)
#plt.show()

#c

fr = 240
d = 1
fr_esan = 2400

t = np.arange(0, d, 1/fr_esan)
semnal_s = np.mod(t, 1/fr)*fr

plt.plot(t, semnal_s)
plt.title('Semnal sawtooth de 240 Hz')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.grid(True)
#plt.show()


#d
frecv = 300
durata_s = 1
frecv_es = 900

timp_square = np.arange(0, durata_s, 1/frecv_es)
semnal_square = np.sign(np.sin(2 * np.pi * frecv_es * timp_square))

plt.plot(timp_square, semnal_square, color='red')
plt.title('Semnal square de 300 Hz')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.grid(True)
#plt.show()

#e- genereasa o imagine 2D(semnal in 2 dimensiuni) cu valori aleatorii
dimensiune = (128, 128)
semnal_2d = np.random.rand(dimensiune[0], dimensiune[1])
plt.imshow(semnal_2d, cmap='Accent', interpolation='none')
plt.title('Semnal 2D Aleator')
plt.colorbar(label='Intensitate')
plt.xlabel('Coloane')
plt.ylabel('Linii')
#plt.show()

#f - imagine 2D unde intensitatea creste diagonal

dimensiune = (128, 128)
semnal_2d = np.zeros(dimensiune)
for i in range(min(dimensiune)):
    semnal_2d[i, i:] = i / min(dimensiune)  # Normalizat între 0 și 1
plt.imshow(semnal_2d, cmap='gray', interpolation='none')
plt.title('Semnal 2D cu Gradient Diagonal')
plt.colorbar(label='Intensitate')
plt.xlabel('Coloane')
plt.ylabel('Linii')
plt.show()

