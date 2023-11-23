import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

# Definirea funcției de atenuare în funcție de SNR
def attenuate_high_frequencies(image, snr_threshold):
    # Calcularea Fourier Transform a imaginii
    image_fft = np.fft.fft2(image)

    # Calcularea spectrului în decibeli
    image_fft_db = 20 * np.log10(np.abs(image_fft))

    # Calcularea mediei și deviației standard a spectrului
    mean_spectrum = np.mean(image_fft_db)
    std_spectrum = np.std(image_fft_db)

    # Calcularea SNR
    snr = mean_spectrum / std_spectrum

    # Atenuarea frecvențelor înalte dacă SNR este mai mare decât pragul
    if snr > snr_threshold:
        # Setarea frecvențelor înalte la zero
        image_fft[image_fft_db > mean_spectrum + snr_threshold * std_spectrum] = 0

    # Calcularea inversă a Fourier Transform
    compressed_image = np.fft.ifft2(image_fft)
    compressed_image = np.real(compressed_image)

    return compressed_image

# Încărcarea imaginii
image = misc.face(gray=True)

# Setarea pragului SNR autoimpus
snr_threshold = 10

# Aplicarea atenuării frecvențelor înalte și afișarea imaginilor
compressed_image = attenuate_high_frequencies(image, snr_threshold)

image = misc.face(gray=True)
plt.imshow(image, cmap='gray')
plt.show()

plt.imshow(compressed_image, cmap='gray')
plt.title(f'Imaginea comprimată cu SNR > {snr_threshold}')
plt.show()