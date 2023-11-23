import numpy as np
import matplotlib.pyplot as plt
from scipy import misc, ndimage
from skimage.util import random_noise
from skimage.metrics import peak_signal_noise_ratio

# Încărcați imaginea originală a ratonului
original_image = misc.face(gray=True)

# Adăugați zgomot impulsional (salt-and-pepper noise) la imagine
noisy_image = random_noise(original_image, mode='s&p', amount=0.05)

# Filtrare cu filtru median pentru eliminarea zgomotului
denoised_image = ndimage.median_filter(noisy_image, size=3)

# Calculați raportul semnal-zgomot (SNR) înainte și după denoise
snr_before = peak_signal_noise_ratio(original_image, noisy_image)
snr_after = peak_signal_noise_ratio(original_image, denoised_image)

# Afișați imaginile și raporturile SNR
plt.figure(figsize=(12, 4))

plt.subplot(131)
plt.imshow(original_image, cmap='gray')
plt.title('Imaginea Originală')

plt.subplot(132)
plt.imshow(noisy_image, cmap='gray')
plt.title('Imaginea cu Zgomot Adăugat')

plt.subplot(133)
plt.imshow(denoised_image, cmap='gray')
plt.title('Imaginea După Filtrare Mediană')

plt.show()

print(f"Raport SNR înainte de denoise: {snr_before:.2f} dB")
print(f"Raport SNR după denoise: {snr_after:.2f} dB")