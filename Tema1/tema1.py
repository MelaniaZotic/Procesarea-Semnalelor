import numpy as np
import matplotlib.pyplot as plt
from scipy import misc, ndimage
from scipy.fft import dctn, idctn

# sarcina 1 - Completați algoritmul JPEG incluzând toate blocurile din imagine.


def jpeg_compress_decompress(image, quantization_matrix, block_size=8):
    # Ma asigur că imaginea este divizibilă după dimensiunea blocului
    height, width = image.shape
    height_padded = height + (block_size - height % block_size) % block_size
    width_padded = width + (block_size - width % block_size) % block_size
    image_padded = np.pad(image, ((0, height_padded - height), (0, width_padded - width)), 'constant')

    # Inițializez imagini comprimate și decomprimate
    compressed_image = np.zeros_like(image_padded)
    decompressed_image = np.zeros_like(image_padded)

    # Aplic DCT și Quantization pe fiecare bloc
    for i in range(0, height_padded, block_size):
        for j in range(0, width_padded, block_size):
            block = image_padded[i:i + block_size, j:j + block_size]
            dct_block = dctn(block, norm='ortho') # Aplicarea transformatei DCT
            quantized_block = np.round(dct_block / quantization_matrix) # Cuantizarea coeficienților DCT
            compressed_image[i:i + block_size, j:j + block_size] = quantized_block

    # Aplic Inverse DCT pentru fiecare bloc
    for i in range(0, height_padded, block_size):
        for j in range(0, width_padded, block_size):
            quantized_block = compressed_image[i:i + block_size, j:j + block_size]
            idct_block = idctn(quantized_block * quantization_matrix, norm='ortho') # Aplicarea transformatei DCT Inverse
            decompressed_image[i:i + block_size, j:j + block_size] = idct_block

    return compressed_image, decompressed_image[:height, :width]


# Incarc o imagine
image = misc.ascent()

# Definesc matricea de cuantizare
quantization_matrix = np.array([
    [80, 60, 50, 80, 120, 160, 200, 240],
    [60, 60, 70, 95, 130, 140, 240, 220],
    [70, 65, 80, 120, 160, 285, 350, 280],
    [70, 85, 110, 145, 255, 435, 400, 248],
    [90, 110, 185, 280, 340, 545, 515, 385],
    [120, 175, 275, 320, 405, 520, 565, 460],
    [245, 320, 390, 435, 515, 605, 600, 505],
    [360, 460, 475, 490, 560, 500, 515, 495]
])

# Aplic JPEG compression si decompression
compressed_image, decompressed_image = jpeg_compress_decompress(image, quantization_matrix)

# Asisez imaginea originala, imaginea compressed si decompressed
plt.figure(figsize=(15, 5))
plt.subplot(131)
plt.imshow(image, cmap=plt.cm.gray)
plt.title('Original Image')
plt.subplot(132)
plt.imshow(compressed_image, cmap=plt.cm.gray)
plt.title('Compressed Image (DCT Coefficients)')
plt.subplot(133)
plt.imshow(decompressed_image, cmap=plt.cm.gray)
plt.title('Decompressed Image')
plt.show()

# sarcina 2 - Extindeți la imagini color (incluzând transformarea din RGB în Y'CbCr). Exemplificați pe scipy.misc.face folosită în tema anterioară.

from skimage import color
from scipy.misc import face

# Functie pentru conversia unei imagini din format RGB in format YCbCr
def rgb2ycbcr(rgb_image):
    return color.rgb2ycbcr(rgb_image)

# Functie pentru conversia unei imagini din format YCbCr inapoi in format RGB
def ycbcr2rgb(ycbcr_image):
    return color.ycbcr2rgb(ycbcr_image)

# Functie pentru aplicarea procesului de compresie si decompresie JPEG pe o imagine color
def apply_jpeg_on_color_image(color_image, quantization_matrix):
    # Converteste imaginea color din RGB in YCbCr
    ycbcr_image = rgb2ycbcr(color_image)

    compressed_channels = []  # Lista pentru stocarea canalelor comprimate
    decompressed_channels = [] # Lista pentru stocarea canalelor decomprimate

    # Proceseaza fiecare canal (Y, Cb, Cr) separat
    for i in range(3):
        channel = ycbcr_image[:, :, i] # Extragere canal individual
        compressed, decompressed = jpeg_compress_decompress(channel, quantization_matrix)
        compressed_channels.append(compressed)
        decompressed_channels.append(decompressed)

    # Combină canalele comprimate si decomprimate inapoi intr-o singura imagine
    compressed_image = np.stack(compressed_channels, axis=-1)
    decompressed_image = np.stack(decompressed_channels, axis=-1)

    # Converteste imaginea decomprimata din YCbCr inapoi in RGB
    decompressed_image_rgb = ycbcr2rgb(decompressed_image)

    return compressed_image, decompressed_image_rgb


# Incarca o imagine color
color_image = face()

# Aplica compresia si decompresia JPEG pe imaginea color
compressed_color_image, decompressed_color_image = apply_jpeg_on_color_image(color_image, quantization_matrix)

# Afiseaza imaginea originala si cea decomprimata
plt.figure(figsize=(10, 5))
plt.subplot(121)
plt.imshow(color_image)
plt.title('Original Color Image')
plt.subplot(122)
plt.imshow(decompressed_color_image)
plt.title('Decompressed Color Image')
plt.show()


# sarcina 3 - Extindeți algoritmul pentru compresia imaginii până la un prag MSE impus de utilizator.
def calculate_mse(image1, image2):

    return np.mean((image1 - image2) ** 2)


def adjust_quantization_for_mse(image, initial_quantization_matrix, mse_threshold, max_iterations=50):

    quantization_matrix = initial_quantization_matrix.copy()
    iteration = 0

    # Buclează până când MSE-ul actual este sub pragul specificat sau se ating max_iterations
    while iteration < max_iterations:
        compressed_image, decompressed_image = jpeg_compress_decompress(image, quantization_matrix)
        current_mse = calculate_mse(image, decompressed_image)

        # Verifică dacă MSE-ul actual este sub pragul dorit
        if current_mse <= mse_threshold:
            break

        # cresc valorile matricei de cuantizare pentru a scădea calitatea
        quantization_matrix += 5
        iteration += 1

    return decompressed_image, quantization_matrix, current_mse

# Definesc un prag MSE mai mic pentru demonstrație
small_mse_threshold = 200

# Aplic compresia JPEG ajustată pentru pragul MSE
adjusted_image, adjusted_quantization_matrix, achieved_mse = adjust_quantization_for_mse(image, quantization_matrix, small_mse_threshold)

# Afisez imaginile
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.imshow(image, cmap=plt.cm.gray)
plt.title('Original Image')
plt.subplot(122)
plt.imshow(adjusted_image, cmap=plt.cm.gray)
plt.title(f'Adjusted Image (MSE: {achieved_mse:.2f})')
plt.show()