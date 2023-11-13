import numpy as np
import matplotlib.pyplot as plt

def generare_semnal(frecventa, amplitudine=1, faza=0, durata=1, frecventa_eșantionare=1):
    timp = np.arange(0, durata, 1/frecventa_eșantionare)
    semnal = amplitudine * np.sin(2 * np.pi * frecventa * timp + faza)
    return timp, semnal

def eșantionare(frecventa_eșantionare, durata=1):
    timp_eșantionat = np.arange(0, durata, 1/frecventa_eșantionare)
    return timp_eșantionat

# Parametri pentru semnalul inițial
frecventa_inițială = 5
amplitudine_inițială = 1
faza_inițială = 0
durata_semnal = 1
frecventa_eșantionare_noua = 20  # Modificare a ratei de eșantionare

# Generare semnal inițial cu noua frecvență de eșantionare
timp_nou, semnal_inițial_nou = generare_semnal(frecventa_inițială, amplitudine_inițială, faza_inițială, durata_semnal, frecventa_eșantionare_noua)

# Eșantionare semnal inițial cu noua frecvență de eșantionare
timp_eșantionat_nou = eșantionare(frecventa_eșantionare_noua, durata_semnal)

# Generare alte două semnale cu frecvențe diferite
frecventa_2 = 2
frecventa_3 = 8
_, semnal_2_nou = generare_semnal(frecventa_2, amplitudine_inițială, faza_inițială, durata_semnal, frecventa_eșantionare_noua)
_, semnal_3_nou = generare_semnal(frecventa_3, amplitudine_inițială, faza_inițială, durata_semnal, frecventa_eșantionare_noua)

# Desenarea graficelor
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(timp_nou, semnal_inițial_nou, label='Semnal Inițial')
plt.title('Semnal Inițial cu noua frecvență de eșantionare')

plt.subplot(3, 1, 2)
plt.plot(timp_eșantionat_nou, semnal_2_nou, label=f'Semnal {frecventa_2} Hz eșantionat cu noua frecvență de eșantionare')
plt.title(f'Semnal {frecventa_2} Hz eșantionat cu noua frecvență de eșantionare')

plt.subplot(3, 1, 3)
plt.plot(timp_eșantionat_nou, semnal_3_nou, label=f'Semnal {frecventa_3} Hz eșantionat cu noua frecvență de eșantionare')
plt.title(f'Semnal {frecventa_3} Hz eșantionat cu noua frecvență de eșantionare')

plt.tight_layout()
plt.savefig("ex3.png")
plt.show()
