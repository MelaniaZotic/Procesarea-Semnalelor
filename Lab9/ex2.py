import numpy as np
import matplotlib.pyplot as plt

# (1) Generarea seriei de timp
np.random.seed(42)

N = 1000
t = np.arange(N)
trend = 0.02 * t ** 2  # componenta trend, ecuație de gradul 2
seasonality = 10 * np.sin(2 * np.pi * t / 50) + 5 * np.cos(2 * np.pi * t / 30)  # două frecvențe pentru sezon
noise = np.random.normal(0, 2, N)  # zgomot alb gaussian

time_series = trend + seasonality + noise

# (2) Medierea exponențială pentru a elimina trend-ul
alpha = 0.1
smoothed_series = np.zeros_like(time_series)

for i in range(N):
    if i == 0:
        smoothed_series[i] = time_series[i]
    else:
        smoothed_series[i] = alpha * time_series[i] + (1 - alpha) * smoothed_series[i - 1]

# Afișarea seriei de timp originală și a celei netede
plt.figure(figsize=(12, 6))
plt.plot(t, time_series, label='Seria de timp originală')
plt.plot(t, smoothed_series, label='Seria de timp netedă')
plt.legend()
plt.title('Seria de timp originală și netedă')
plt.savefig("ex2.png")

plt.show()