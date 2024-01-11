import numpy as np
import matplotlib.pyplot as plt

# Parameters for the unidimensional Gaussian distribution
mean_uni = 0  # Placeholder mean
variance_uni = 1  # Placeholder variance

# Generate a sample from the unidimensional Gaussian distribution
sample_uni = np.random.normal(mean_uni, np.sqrt(variance_uni), 1000)

# Plot the unidimensional distribution
plt.figure(figsize=(10, 5))
plt.hist(sample_uni, bins=30, density=True, alpha=0.6, color='g')
plt.title('Unidimensional Gaussian Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Parameters for the bidimensional Gaussian distribution
mean_bi = [0, 0]  # Placeholder mean vector
covariance_bi = [[1, 0], [0, 1]]  # Placeholder covariance matrix

# Generate a sample from the bidimensional Gaussian distribution
sample_bi = np.random.multivariate_normal(mean_bi, covariance_bi, 1000)

# Plot the bidimensional distribution
plt.figure(figsize=(10, 5))
plt.scatter(sample_bi[:, 0], sample_bi[:, 1], alpha=0.5)
plt.title('Bidimensional Gaussian Distribution')
plt.xlabel('X value')
plt.ylabel('Y value')
plt.grid(True)
plt.axis('equal')  # Equal scaling by x and y axes
plt.show()