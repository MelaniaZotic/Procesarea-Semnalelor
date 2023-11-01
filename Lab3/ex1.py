import numpy as np
import matplotlib.pyplot as plt


# funcție care generează matricea Fourier
def fourier(n):
    f = np.zeros((n, n), dtype=np.complex128)
    for m in range(n):
        for k in range(n):
            f[m, k] = np.exp(2 * np.pi * 1j * m * k / n)
    return f


n = 8
f = fourier(n)


# Creează un set de subploturi cu dim rânduri și 2 coloane
def plot_matrix(dim, f):
    n = np.linspace(0, dim - 1, dim)
    fig, axs = plt.subplots(dim, 2)
    plt.suptitle("Partea reala si partea imaginara")

    for i, semnal in enumerate(n):
        axs[i][0].plot(n, np.real(f[i]))
        axs[i][1].plot(n, np.imag(f[i]), '--')
        axs[i][0].grid()
        axs[i][1].grid()
    plt.savefig("ex1.png")
    plt.show()
    plt.close(fig)


plot_matrix(n, f)


# funcția verifică dacă o matrice este unitară
# O matrice complexă este unitară dacă produsul ei cu conjugata transpusă este egal cu identitatea
# Aceasta este o funcție care verifică dacă toate elementele a două matrice sunt apropiate în ceea ce privește valorile lor.

def unit_matrix(f):
    return np.iscomplexobj(f) and np.allclose(np.dot(f, np.conj(f).T), np.dot(n, np.identity(n)))


if unit_matrix(f):
    print("Matricea Fourier este unitara")
else:
    print("Matricea Fourier nu este unitara")
