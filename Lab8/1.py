import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error

# (a) Generarea și desenarea seriei de timp
def generate_time_series():
    np.random.seed(42)
    N = 1000
    t = np.arange(N)

    # Componenta de trend
    trend = 0.02 * t**2

    # Două frecvențe pentru sezon
    seas_freq1 = 0.02
    seas_freq2 = 0.005
    seasonality = 10 * np.sin(2 * np.pi * seas_freq1 * t) + 5 * np.sin(2 * np.pi * seas_freq2 * t)

    # Variabilitate mică folosind zgomot alb gaussian
    noise = np.random.normal(0, 1, N)

    # Serie de timp finală
    time_series = trend + seasonality + noise

    # Desenarea componentelor individuale și a seriei de timp complete
    plt.figure(figsize=(12, 6))
    plt.plot(t, trend, label='Trend', color='blue')  # Adăugați această linie pentru trend
    plt.plot(t, seasonality, label='Seasonality', color='green')  # Colorați sezonul în verde
    plt.plot(t, time_series, label='Time Series', color='black')  # Colorați seria de timp în negru
    plt.legend()
    plt.title('Generated Time Series')
    plt.show()

    return time_series

# (b) Calcularea și desenarea autocorelației
def plot_autocorrelation(time_series):
    autocorrelation = acf(time_series, nlags=len(time_series)-1)

    # Desenarea autocorelației
    plt.figure(figsize=(12, 6))
    plt.stem(autocorrelation)
    plt.title('Autocorrelation of Time Series')
    plt.xlabel('Lag')
    plt.ylabel('Autocorrelation')
    plt.show()

# (c) Calcularea și afișarea modelului AR
def fit_and_plot_ar_model(time_series, p=10):
    model = AutoReg(time_series, lags=p)
    result = model.fit()

    print(result.summary())

    # Afișarea seriei de timp originală și a predicțiilor
    plt.figure(figsize=(12, 6))
    plt.plot(time_series, label='Original Time Series')
    plt.plot(result.predict(start=p, end=len(time_series)-1), label='AR Model Prediction')
    plt.legend()
    plt.title('AR Model Prediction')
    plt.show()

# (d) Tunarea hiperparametrilor pentru predictia AR
def hyperparameter_tuning(time_series):
    best_m = 0
    best_p = 0
    best_mse = float('inf')

    for p in range(1, 21):
        for m in range(1, 21):
            model = AutoReg(time_series, lags=p)
            result = model.fit()

            # Obținem predicțiile pentru viitorul imediat
            predictions = result.predict(start=len(time_series), end=len(time_series)+m-1)

            # Calculăm eroarea medie pătratică (MSE)
            mse = mean_squared_error(time_series[p:], predictions)

            # Actualizăm cele mai bune parametri dacă găsim un MSE mai mic
            if mse < best_mse:
                best_mse = mse
                best_p = p
                best_m = m

    # Afișăm rezultatele
    print(f'Best lag order (p): {best_p}')
    print(f'Best forecast horizon (m): {best_m}')
    print(f'Best MSE: {best_mse}')

# Apelarea funcțiilor
time_series_data = generate_time_series()
plot_autocorrelation(time_series_data)
fit_and_plot_ar_model(time_series_data)
hyperparameter_tuning(time_series_data)