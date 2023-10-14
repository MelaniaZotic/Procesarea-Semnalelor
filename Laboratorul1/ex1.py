import numpy as np
import matplotlib.pyplot as plt


#Intervalul de timp cerut în enunt

t = np.arange(0, 0.03 + 0.0005, 0.0005)
#Semnalele continue din enunt

x_t = np.cos(520 * np.pi * t + np.pi/3)
y_t = np.cos(280 * np.pi * t - np.pi/3)
z_t = np.cos(120 * np.pi * t + np.pi/3)


plt.figure(figsize=(14, 12))
plt.subplot(3, 1, 1)
plt.plot(t, x_t, color='black')
plt.title('x(t) = cos(520πt + π/3)')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, y_t, color='red')
plt.title('y(t) = cos(280πt - π/3)')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, z_t)
plt.title('z(t) = cos(120πt + π/3)')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.grid(True)

plt.tight_layout()
plt.show()

#c

# Frecventa de esantionare
f_s = 200  # Hz din enunt
T_s = 1 / f_s  # perioada de esantionare(cu alte cuvinte, inversul frecventei)

n = np.arange(0, 0.03, T_s) # vector de esantionare


#Esantionarea semnalelor
x_n = np.cos(520 * np.pi * n+ np.pi/3)
y_n = np.cos(280 * np.pi * n - np.pi/3)
z_n = np.cos(120 * np.pi * n + np.pi/3)

plt.figure(figsize=(12, 10))

plt.subplot(3, 1, 1)
plt.stem(n, x_n, linefmt='y-', markerfmt='go', basefmt='b-', use_line_collection=True)
plt.title(r'$x[n] = \cos(520\pi n T_s + \pi/3)$')
plt.xlabel('Eșantioane n')
plt.ylabel('Amplitudine')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n, y_n, linefmt='g-', markerfmt='ro', basefmt='b-', use_line_collection=True)
plt.title(r'$y[n] = \cos(280\pi n T_s - \pi/3)$')
plt.xlabel('Eșantioane n')
plt.ylabel('Amplitudine')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(n, z_n, linefmt='b-', markerfmt='go', basefmt='r-', use_line_collection=True)
plt.title(r'$z[n] = \cos(120\pi n T_s + \pi/3)$')
plt.xlabel('Eșantioane n')
plt.ylabel('Amplitudine')
plt.grid(True)

plt.tight_layout()
plt.show()