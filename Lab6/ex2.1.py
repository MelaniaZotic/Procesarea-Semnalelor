import numpy as np
import matplotlib.pyplot as plt

# Generarea coeficienților polinoamelor p(x) și q(x)
N = 5  # Gradul maxim al polinoamelor
p_coeff = np.random.randint(-10, 10, size=N + 1)
q_coeff = np.random.randint(-10, 10, size=N + 1)

# Calculul produsului utilizând convoluția
r_convolution = np.convolve(p_coeff, q_coeff, mode='full')

# Afișarea rezultatelor
print("Coeficienții polinomului rezultat folosind convoluția:")
print(r_convolution)

# Afisare grafica
plt.plot(r_convolution, marker='o')
plt.title('Produsul polinoamelor folosind convoluția')
plt.show()

# Calculul produsului utilizând înmulțirea directă a coeficienților
r_direct = np.polymul(p_coeff, q_coeff)

# Afișarea rezultatelor
print("Coeficienții polinomului rezultat folosind înmulțirea directă:")
print(r_direct)

# Afisare grafica
plt.plot(r_direct, marker='o')
plt.title('Produsul polinoamelor folosind înmulțirea directă')
plt.show()
# Calculul produsului utilizând FFT
r_fft = np.fft.ifft(np.fft.fft(p_coeff) * np.fft.fft(q_coeff)).real

# Afișarea rezultatelor
print("Coeficienții polinomului rezultat folosind FFT:")
print(r_fft)

# Afisare grafica
plt.plot(r_fft, marker='o')
plt.title('Produsul polinoamelor folosind FFT')
plt.show()
