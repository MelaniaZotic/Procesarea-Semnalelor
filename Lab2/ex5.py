import numpy as np
import sounddevice as sd

# Frecvente ale celor două semnale
frecventa1 = 440  # Frecvența în Hz pentru primul semnal
frecventa2 = 660  # Frecvența în Hz pentru al doilea semnal

# Durata și frecvența de eșantionare
durata = 3  # Durata în secunde
frecventa_eșantionare = 44100  # Frecvența de eșantionare în Hz

# Generează semnalele
t = np.linspace(0, durata, durata * frecventa_eșantionare, endpoint=False)
semnal1 = np.sin(2 * np.pi * frecventa1 * t)
semnal2 = np.sin(2 * np.pi * frecventa2 * t)

# Concatenează cele două semnale
semnal_final = np.concatenate((semnal1, semnal2))

# Normalizare la intervalul [-1, 1]
semnal_final = semnal_final / np.max(np.abs(semnal_final))

# Redă sunetul rezultat
sd.play(semnal_final, frecventa_eșantionare)
sd.wait()