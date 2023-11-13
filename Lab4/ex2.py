import numpy as np
import matplotlib.pyplot as plt


# Această funcție generează un semnal sinusoidal cu parametri specificați.
def generare_semnal(frecventa, amplitudine=1, faza=0, durata=1, frecventa_esantionare=1):
    timp = np.arange(0, durata, 1 / frecventa_esantionare)
    semnal = amplitudine * np.sin(2 * np.pi * frecventa * timp + faza)
    return timp, semnal


# Această funcție realizează eșantionarea semnalului cu o anumită rată de eșantionare
def eșantionare(frecventa_esantionare, durata=1):
    timp_eșantionat = np.arange(0, durata, 1 / frecventa_esantionare)
    return timp_eșantionat


# Parametri pentru semnalul inițial
frecventa_initala = 5
amplitudine_initiala = 1
faza_initiala = 0
durata_semnal = 1
frecventa_esantionare = 8

# Generare semnal inițial
timp, semnal_inițial = generare_semnal(frecventa_initala, amplitudine_initiala, faza_initiala, durata_semnal,
                                       frecventa_esantionare)

# Eșantionare sub-Nyquist
sub_nyquist = frecventa_initala / 2
timp_eșantionat = eșantionare(frecventa_esantionare, durata_semnal)

# Generare alte două semnale cu frecvențe diferite
frecventa_2 = 2
frecventa_3 = 8
_, semnal_2 = generare_semnal(frecventa_2, amplitudine_initiala, faza_initiala, durata_semnal, frecventa_esantionare)
_, semnal_3 = generare_semnal(frecventa_3, amplitudine_initiala, faza_initiala, durata_semnal, frecventa_esantionare)

# Desenarea graficelor
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(timp, semnal_inițial, label='Semnal Inițial')
plt.title('Semnal Inițial')

plt.subplot(3, 1, 2)
plt.plot(timp_eșantionat, semnal_2, label=f'Semnal {frecventa_2} Hz eșantionat sub-Nyquist')
plt.title(f'Semnal {frecventa_2} Hz eșantionat sub-Nyquist')

plt.subplot(3, 1, 3)
plt.plot(timp_eșantionat, semnal_3, label=f'Semnal {frecventa_3} Hz eșantionat sub-Nyquist')
plt.title(f'Semnal {frecventa_3} Hz eșantionat sub-Nyquist')

plt.tight_layout()
plt.savefig("ex2.png")
plt.show()
