import numpy as np
import matplotlib.pyplot as plt

#Definirea parametrilor:
amplitudine = 1
frecventa = 5
faza = np.pi / 4
t = np.arange(0, 1, 0.01)

semnal_sinus = amplitudine * np.sin(2 * np.pi * frecventa * t + faza)
semnal_cosinus = amplitudine * np.sin(2 * np.pi * frecventa * t + faza + np.pi/2)

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

