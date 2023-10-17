import numpy as np
import matplotlib.pyplot as plt
#c

f_s = 200
T_s = 1 / f_s

n = np.arange(0, 0.03, T_s)

x_n = np.cos(520 * np.pi * n + np.pi/3)
y_n = np.cos(280 * np.pi * n - np.pi/3)
z_n = np.cos(120 * np.pi * n + np.pi/3)

plt.figure(figsize=(16, 14))
plt.subplot(3, 1, 1)
plt.stem(n, x_n)
plt.title('x(n) = cos(520*pi*t + pi/3)')
plt.xlabel('Eșantioane n')
plt.ylabel('x_n')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n, y_n)
plt.title('y(n) = cos(280*pi*t - pi/3)')
plt.xlabel('Eșantioane n')
plt.ylabel('y_n')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(n, z_n)
plt.title('z(n) = cos(120*pi*t - pi/3)')
plt.xlabel('Eșantioane n')
plt.ylabel('z_n')
plt.grid(True)
#plt.show()


#a,b
t = np.arange(0, 0.03, 0.0005)

x_t = np.cos(520 * np.pi * t + np.pi/3)
y_t = np.cos(280 * np.pi * t - np.pi/3)
z_t = np.cos(120 * np.pi * t + np.pi/3)


plt.figure(figsize=(16, 14))
plt.subplot(3, 1, 1)
plt.plot(t, x_t, color='black')
plt.title('x(t) = cos(520*pi*t + pi/3)')
plt.xlabel('t')
plt.ylabel('x_t')
plt.stem(n, x_n, markerfmt='go')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, y_t, color='red')
plt.title('y(t) = cos(280*pi*t - pi/3)')
plt.xlabel('t')
plt.ylabel('y_t')
plt.stem(n, y_n, markerfmt='go')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, z_t)
plt.title('z(t) = cos(120*pi*t + pi/3)')
plt.xlabel('t')
plt.ylabel('z_t')
plt.stem(n, z_n, markerfmt='go')
plt.grid(True)

plt.show()

