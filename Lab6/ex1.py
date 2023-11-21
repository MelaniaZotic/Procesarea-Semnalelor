import numpy as np
import matplotlib.pyplot as plt

# Generarea unui vector aleator x[n] de dimensiune N = 100
N = 100
x = np.random.random(N)


# Calculul iterat al convoluției x ← x * x de trei ori
for i in range(3):
    x = np.convolve(x, x, mode='full')

# Afișarea celor patru grafice
plt.figure(figsize=(12, 8))

# Graficul 1: Vectorul original x[n]
plt.subplot(2, 2, 1)
plt.plot(np.arange(N), x[:N])
plt.title('Vectorul original x[n]')
plt.xlabel('n')
plt.ylabel('x[n]')

# Graficul 2: Convoluția x ← x * x
plt.subplot(2, 2, 2)
plt.plot(np.arange(len(x)), x)
plt.title('Convoluția x ← x * x')
plt.xlabel('n')
plt.ylabel('x[n]')

plt.show()