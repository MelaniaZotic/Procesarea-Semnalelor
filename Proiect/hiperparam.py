import glob
import cv2
import numpy as np
import albumentations as A
import matplotlib.pyplot as plt
from sklearn.model_selection import ParameterGrid
from skimage.metrics import structural_similarity as ssim


# Funcția pentru aplicarea algoritmului Sobel
def apply_sobel(image):
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
    sobel = np.sqrt(sobelx ** 2 + sobely ** 2)
    return np.uint8(sobel / sobel.max() * 255)


# Funcția pentru aplicarea algoritmului Canny
def apply_canny(image, low_threshold, high_threshold):
    return cv2.Canny(image, low_threshold, high_threshold)


# Funcția de evaluare folosind SSIM
def evaluate(true_edges, detected_edges):
    return ssim(true_edges, detected_edges, data_range=255)


# Definirea transformărilor de augmentare
augmentations = A.Compose([
    A.Rotate(limit=20, p=0.5),
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.5)
])

# Calea către directorul cu imagini și către directorul cu true_edges
image_directory = 'D:\\facultate an4\\Procesarea-Semnalelor\\Proiect\\img\\'
true_edges_directory = 'D:\\facultate an4\\Procesarea-Semnalelor\\Proiect\\gt\\'

# Încărcarea automată a imaginilor și a marginilor adevărate
image_paths = sorted(glob.glob(image_directory + '*.png'))
true_edge_paths = sorted(glob.glob(true_edges_directory + '*.png'))

# Încărcăm imaginile și ground truth
images = [cv2.imread(path, cv2.IMREAD_GRAYSCALE) for path in image_paths]
true_edges = [cv2.imread(path, cv2.IMREAD_GRAYSCALE) for path in true_edge_paths]

# Setul de hiperparametri pentru Canny
param_grid = {
    'low_threshold': [50, 100, 150],
    'high_threshold': [150, 200, 250]
}

# Evaluarea Sobel pe toate imaginile
sobel_scores = []
for img, te in zip(images, true_edges):
    sobel_edges = apply_sobel(img)
    score = evaluate(te, sobel_edges)
    sobel_scores.append(score)

average_sobel_score = np.mean(sobel_scores)
print(f"Average Sobel Score: {average_sobel_score}")

# Tunarea și evaluarea Canny pe toate imaginile cu augmentări
best_score = -1
best_params = None

for params in ParameterGrid(param_grid):
    canny_scores = []
    for img, te in zip(images, true_edges):
        # Aplică augmentarea
        augmented_image = augmentations(image=img)['image']

        # Aplică algoritmul Canny pe imaginea augmentată
        canny_edges = apply_canny(augmented_image, **params)

        # Evaluează marginile detectate
        score = evaluate(te, canny_edges)
        canny_scores.append(score)

    mean_score = np.mean(canny_scores)
    if mean_score > best_score:
        best_score = mean_score
        best_params = params

print(f"Best Canny Score: {best_score} with params {best_params}")

average_canny_score_best = best_score
if average_canny_score_best > average_sobel_score:
    print("Canny is closer to true edges.")
else:
    print("Sobel is closer to true edges.")

# Vizualizarea unei imagini exemplu cu marginile detectate folosind Sobel și Canny cu cei mai buni parametri
example_img = images[0]
example_true_edges = true_edges[0]

sobel_example = apply_sobel(example_img)
canny_example = apply_canny(example_img, **best_params)

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(example_img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(sobel_example, cmap='gray')
plt.title('Sobel Edges')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(canny_example, cmap='gray')
plt.title('Canny Edges (Best Params)')
plt.axis('off')

plt.show()


