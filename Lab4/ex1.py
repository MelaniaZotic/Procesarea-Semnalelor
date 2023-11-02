import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import timeit


# funcție care generează matricea Fourier
def fourier(n):
    f = np.zeros((n, n), dtype=np.complex128)
    for m in range(n):
        for k in range(n):
            f[m, k] = np.exp(-2 * np.pi * 1j * m * k / n)
    return f


# funcție care calculează DFT utilizând matricea Fourier
def dft(x):
    n = len(x)
    f = fourier(n)
    return np.dot(f, x)


# Definim dimensiunile pentru care vrem să testăm DFT
N = [128, 256, 512, 1024, 2048, 4096]

# Inițializăm listele pentru a stoca timpii de execuție
times_custom = []
times_numpy = []

# Numărul de repetări pentru timeit
num_repeats = 5

print("Compararea timpilor de execuție (în milisecunde):")
print("{:<8} {:<20} {:<20}".format("N", "Implementare proprie", "numpy.fft"))

# timeit pentru a măsura cât timp durează fiecare funcție să execute DFT pe un vector de lungime n, cu valorile lui n
# luate din lista N.
# Calculăm DFT pentru fiecare dimensiune a vectorului și măsurăm timpul de execuție

# Pentru fiecare valoare a lui n din lista N, codul generează un vector complex aleator x și măsoară timpul de execuție
# pentru dft(x) (implementarea proprie) și np.fft.fft(x) (implementarea NumPy), apoi le adaugă în listele respective.
for n in N:
    x = np.random.random(n) + 1j * np.random.random(n)

    # Timpul pentru implementarea proprie
    custom_time = timeit.timeit('dft(x)', globals=globals(), number=num_repeats) / num_repeats
    times_custom.append(custom_time)

    # Timpul pentru implementarea numpy
    numpy_time = timeit.timeit('np.fft.fft(x)', globals=globals(), number=num_repeats) / num_repeats
    times_numpy.append(numpy_time)

    # Printăm timpul în milisecunde
    print("{:<8d} {:<20.5f} {:<20.5f}".format(n, custom_time * 1000, numpy_time * 1000))

# Convertim secundele în milisecunde pentru plot
times_custom_ms = [t * 1000 for t in times_custom]
times_numpy_ms = [t * 1000 for t in times_numpy]

plt.figure(figsize=(10, 5))
plt.plot(N, times_custom_ms, label='Implementarea proprie', marker='o')
plt.plot(N, times_numpy_ms, label='numpy.fft', marker='x')

# Setăm scara logaritmică pentru axa Oy în baza 10
plt.yscale('log', base=10)  # Corectăm 'basey' în 'base'
plt.gca().yaxis.set_major_formatter(ticker.ScalarFormatter())

# Adăugăm titlul și etichetele axelor
plt.title('Compararea timpilor de execuție DFT vs. numpy.fft în milisecunde')
plt.xlabel('Dimensiunea vectorului N')
plt.ylabel('Timp de execuție (ms, scala logaritmică)')

# Adăugăm legenda
plt.legend()

# Afișăm graficul
plt.show()
