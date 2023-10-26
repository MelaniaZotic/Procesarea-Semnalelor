import numpy as np
import matplotlib.pyplot as plt

N = 8
F = np.zeros((N, N), dtype=complex)
t = np.linspace(0, 1, 8)

x_sin = np.sin(2*np.pi*50*t)

for k in range(N):
    for n in range(N):
        F[k, n] = x_sin[n] * np.exp(-2j * np.pi * k * (n / N))



plt.figure(figsize=(12, 8))

for k in range(N):
    plt.subplot(N, 2, 2*k + 1)
    plt.stem(F[k].real, linefmt='g-', markerfmt='go', basefmt=" ", use_line_collection=True)
    plt.title(f"Partea reală a liniei {k}")

    plt.subplot(N, 2, 2*k + 2)
    plt.stem(F[k].imag, use_line_collection=True)
    plt.title(f"Partea imaginară a liniei {k}")

plt.tight_layout()
plt.show()

I = np.dot(F, F.conj().T)

# Pentru a verifica, calculez norma Frobenius a diferenței dintre I și matricea identitate.
norm = np.linalg.norm(I - np.eye(N))

if norm < 1e-10:
    print("Matricea este unitară!")
else:
    print("Matricea NU este unitară!")

