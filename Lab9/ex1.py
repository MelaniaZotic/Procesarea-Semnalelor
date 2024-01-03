import numpy as np
import matplotlib.pyplot as plt

# Generarea seriei de timp
np.random.seed(42)

N = 1000
t = np.arange(N)
trend = 0.02 * t ** 2
seasonality = 10 * np.sin(2 * np.pi * t / 50) + 5 * np.cos(2 * np.pi * t / 30)
noise = np.random.normal(0, 2, N)

time_series = trend + seasonality + noise

# Desenarea seriei de timp și componentelor separat
plt.figure(figsize=(12, 6))
plt.subplot(4, 1, 1)
plt.plot(t, time_series, label='Seria de timp generată')
plt.legend()
plt.title('Seria de timp generată')

plt.subplot(4, 1, 2)
plt.plot(t, trend, label='Trend')
plt.legend()
plt.title('Trend')

plt.subplot(4, 1, 3)
plt.plot(t, seasonality, label='Sezon')
plt.legend()
plt.title('Sezon')

plt.subplot(4, 1, 4)
plt.plot(t, noise, label='Zgomot')
plt.legend()
plt.title('Zgomot')

plt.tight_layout()
plt.savefig("ex1.png")
plt.show()