import numpy as np
import matplotlib.pyplot as plt

# Definirea dimensiunilor
N = 256
n1 = np.arange(N)
n2 = np.arange(N)

# Definirea funcțiilor
x1 = np.sin(2 * np.pi * np.outer(n1, np.ones(N)) + 3 * np.pi * np.outer(np.ones(N), n2))
x2 = np.sin(4 * np.pi * np.outer(n1, np.ones(N))) + np.cos(6 * np.pi * np.outer(np.ones(N), n2))

# Afisarea imaginilor
plt.imshow(x1, cmap='gray')
plt.title('Imagina pentru sin(2πn1 + 3πn2)')
plt.show()

plt.imshow(x2, cmap='gray')
plt.title('Imagina pentru sin(4πn1) + cos(6πn2)')
plt.show()

# Calcularea Fourier Transform și afișarea spectrului
X1 = np.fft.fft2(x1)
X2 = np.fft.fft2(x2)

# Calculul spectrului în decibeli
X1_db = 20 * np.log10(np.abs(X1))
X2_db = 20 * np.log10(np.abs(X2))

plt.imshow(X1_db, cmap='gray')
plt.title('Spectru pentru sin(2πn1 + 3πn2)')
plt.colorbar()
plt.show()

plt.imshow(X2_db, cmap='gray')
plt.title('Spectru pentru sin(4πn1) + cos(6πn2)')
plt.colorbar()
plt.show()

# Definirea funcțiilor Y conform descrierii date
Y1 = np.zeros((N, N))
Y1[0, 5] = Y1[N-5, 0] = Y1[N-5, N-5] = 1

Y2 = np.zeros((N, N))
Y2[5, 0] = Y2[N-5, 0] = Y2[N-5, N-5] = 1

# Afisarea imaginilor Y
plt.imshow(Y1, cmap='gray')
plt.title('Imaginea pentru Y conform descrierii')
plt.show()

plt.imshow(Y2, cmap='gray')
plt.title('Imaginea pentru Y conform descrierii')
plt.show()

# Calcularea Fourier Transform și afișarea spectrului pentru Y
Y1_fft = np.fft.fft2(Y1)
Y2_fft = np.fft.fft2(Y2)

Y1_db = 20 * np.log10(np.abs(Y1_fft))
Y2_db = 20 * np.log10(np.abs(Y2_fft))

plt.imshow(Y1_db, cmap='gray')
plt.title('Spectru pentru Y conform descrierii')
plt.colorbar()
plt.show()

plt.imshow(Y2_db, cmap='gray')
plt.title('Spectru pentru Y conform descrierii')
plt.colorbar()
plt.show()