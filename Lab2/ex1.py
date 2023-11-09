import numpy as np
import matplotlib.pyplot as plt

#Definirea parametrilor:
# Amplitudinea semnalului (înălțimea maximă).
amplitudine = 1
frecventa = 5 # Numărul de oscilații complete într-o secundă.
faza = np.pi / 4 # Deplasarea semnalului pe axa orizontală.
t = np.arange(0, 1, 0.01) # Un vector de timp care începe de la 0 și se termină la 1, cu un pas de 0,01 secunde.

semnal_sinus = amplitudine * np.sin(2 * np.pi * frecventa * t + faza) # semnal sinosidal
semnal_cosinus = amplitudine * np.sin(2 * np.pi * frecventa * t + faza + np.pi/2) # semnal sinusoidal cu o replasare de pi/2 astfel e transformat in cosinus


plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(t, semnal_sinus, label="Sinus", color="blue")
plt.title("Semnal sinusoidal")
plt.xlabel("Timp")
plt.ylabel("Amplitudine")
plt.legend()


plt.subplot(2, 1, 2)
plt.plot(t, semnal_cosinus, label="Cosinus", color="blue")
plt.title("Semnal cosinus")
plt.xlabel("Timp")
plt.ylabel("Amplitudine")
plt.legend()
plt.show()

