import numpy as np
import matplotlib.pyplot as plt

# Dimensiunea seriei de timp
N = 1000

# Generarea timpului
time = np.arange(N)

# Componenta trend (ecuație de gradul 2)
trend = 0.02 * time**2 + 0.5 * time + 10

# Componenta sezon (două frecvențe)
seasonality = 5 * np.sin(2 * np.pi * time / 100) + 3 * np.cos(2 * np.pi * time / 50)

# Componenta de zgomot alb gaussian
noise = np.random.normal(0, 1, N)

# Seria de timp totală ca sumă a celor trei componente
time_series = trend + seasonality + noise

# Calculați vectorul de autocorelație
autocorrelation = np.correlate(time_series, time_series, mode='full')

# Normalizează vectorul de autocorelație pentru a obține corelații în intervalul [-1, 1]
autocorrelation /= np.max(autocorrelation)

# Desenează vectorul de autocorelație
plt.figure(figsize=(12, 4))
plt.stem(autocorrelation, use_line_collection=True)
plt.title('Vectorul de autocorelație')
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')
plt.show()