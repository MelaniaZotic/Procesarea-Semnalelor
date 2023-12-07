import numpy as np
import matplotlib.pyplot as plt

# Dimensiunea seriei de timp
N = 1000

# Generarea timpului
time = np.arange(N)

# Componenta trend (ecuație de gradul 2)
trend = 0.02 * time**2 + 0.5 * time + 10

# Componenta season (două frecvențe)
seasonality = 5 * np.sin(2 * np.pi * time / 100) + 3 * np.cos(2 * np.pi * time / 50)

# Componenta de zgomot alb gaussian
noise = np.random.normal(0, 1, N)

# Seria de timp totală ca sumă a celor trei componente
time_series = trend + seasonality + noise

# Desenarea seriilor de timp și componentelor separate
plt.figure(figsize=(12, 6))

# Componenta trend
plt.subplot(3, 1, 1)
plt.plot(time, trend, label='Trend')
plt.legend()

# Componenta sezon
plt.subplot(3, 1, 2)
plt.plot(time, seasonality, label='Seasonality')
plt.legend()

# Componenta de zgomot
plt.subplot(3, 1, 3)
plt.plot(time, noise, label='Noise')
plt.legend()

plt.tight_layout()
plt.show()

# Desenarea seriei de timp complete
plt.figure(figsize=(12, 4))
plt.plot(time, time_series, label='Time Series')
plt.title('Seria de timp generată')
plt.legend()
plt.show()