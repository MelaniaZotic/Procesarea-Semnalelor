import numpy as np
import matplotlib.pyplot as plt

def construct_window(window_type, window_size):
    if window_type == "rectangular":
        return np.ones(window_size)
    elif window_type == "hanning":
        return np.hanning(window_size)
    else:
        raise ValueError("Invalid window type")

def plot_window_and_signal(window, signal, title):
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 1, 1)
    plt.plot(window)
    plt.title(f"{title} Window")

    plt.subplot(2, 1, 2)
    plt.plot(signal)
    plt.title("Sinusoidal Signal")

    plt.tight_layout()
    plt.show()

# Parametrii
f = 100        # Frecvența sinusoidală
A = 1          # Amplitudinea
phi = 0        # Faza
Nw = 200       # Dimensiunea ferestrei

# Construirea ferestrelor
rectangular_window = construct_window("rectangular", Nw)
hanning_window = construct_window("hanning", Nw)

# Construirea semnalului sinusoidal
t = np.arange(Nw)
sinusoidal_signal = A * np.sin(2 * np.pi * f * t / Nw + phi)

# Aplicarea ferestrei la semnal
rectangular_windowed_signal = rectangular_window * sinusoidal_signal
hanning_windowed_signal = hanning_window * sinusoidal_signal

# Afisarea ferestrelor si a semnalului
plot_window_and_signal(rectangular_window, rectangular_windowed_signal, "Rectangular")
plot_window_and_signal(hanning_window, hanning_windowed_signal, "Hanning")