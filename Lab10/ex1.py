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

mean_of_sample_uni = np.mean(sample_uni)
print(mean_of_sample_uni)
