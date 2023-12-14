import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# (a) Generarea seriei de timp
np.random.seed(42)

N = 1000
t = np.arange(N)
trend = 0.02 * t ** 2  # componenta trend, ecuație de gradul 2
seasonality = 10 * np.sin(2 * np.pi * t / 50) + 5 * np.cos(2 * np.pi * t / 30)  # două frecvențe pentru sezon
noise = np.random.normal(0, 2, N)  # zgomot alb gaussian

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
plt.show()

# (b) Calculul vectorului de autocorelație
acf = sm.tsa.acf(time_series, nlags=40)  # nlags reprezintă numărul de întârzieri în calculul autocorelației

# Desenarea vectorului de autocorelație
plt.figure(figsize=(12, 6))
plt.stem(acf, use_line_collection=True)
plt.title('Vectorul de autocorelație')
plt.xlabel('Întârzieri')
plt.show()

# (c) Calculul modelului AR
order = 10  # dimensiunea modelului AR (poți ajusta acest parametru)
model = sm.tsa.AR(time_series).fit(maxlag=order)

# Afișarea seriei de timp originală și predicțiile
predictions = model.predict(start=order, end=N - 1)
plt.figure(figsize=(12, 6))
plt.plot(t, time_series, label='Seria de timp originală')
plt.plot(t[order:], predictions, label='Predictii AR')
plt.legend()
plt.title('Seria de timp originală și predicțiile AR')
plt.show()

# (d) Găsirea celui mai bun orizont de predictie (hyperparameter tuning)
best_mse = np.inf
best_m = 0

for m in range(1, 21):  # Încercați diferite valori ale orizontului de predictie (1 la 20)
    predictions = model.predict(start=order, end=N - 1 + m)
    mse = np.mean((time_series[order:] - predictions[:-m]) ** 2)

    if mse < best_mse:
        best_mse = mse
        best_m = m

print(f'Cel mai bun orizont de predictie: {best_m}')