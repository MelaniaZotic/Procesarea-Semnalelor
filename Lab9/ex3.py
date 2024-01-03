import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

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

# (3) Generarea modelului MA cu orizont q
q = 5
ma_model = sm.tsa.ARIMA(smoothed_series, order=(0, 0, q)).fit()

# (4) Generarea modelului ARMA cu orizont p și q
p, q = 2, 2
arma_model = sm.tsa.ARIMA(smoothed_series, order=(p, 0, q)).fit()

# Afișarea rezultatelor pentru modelele MA și ARMA
plt.figure(figsize=(12, 6))
plt.plot(t, smoothed_series, label='Seria de timp netedă')
plt.plot(t[:len(ma_model.fittedvalues)], ma_model.fittedvalues, label=f'Model MA (q={q})')
plt.plot(t[:len(arma_model.fittedvalues)], arma_model.fittedvalues, label=f'Model ARMA (p={p}, q={q})')
plt.legend()
plt.title('Model MA și ARMA pe seria de timp netedă')
plt.show()