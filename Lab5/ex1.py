import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# a - frecventa de esantionare

# Citirea datelor din fișierul CSV
df = pd.read_csv('Train.csv')

# Convertirea coloanei 'Datetime' în tip de date datetime
df['Datetime'] = pd.to_datetime(df['Datetime'], format='%d-%m-%Y %H:%M')

# Calculul diferențelor de timp în secunde folosind shift()
time_diff_seconds = (df['Datetime'] - df['Datetime'].shift(1)).dt.total_seconds()

# Calculul frecvenței de eșantionarew
sampling_frequency = 1 / np.mean(time_diff_seconds / 3600)

print(f"Frecventa de esantionare: {sampling_frequency} esantioane/ora")

# b
# Calculul intervalului de timp acoperit de esantioane
# Această linie de cod calculează diferența dintre ultimul și primul element al indexului Datetime,
time_interval = df['Datetime'].iloc[-1] - df['Datetime'].iloc[0]

print(f"Intervalul de timp acoperit de esantioane: {time_interval}")

# c - Frecventa maxima in semnal

# Semnalul pe care îl analizăm (a treia coloană din fișierul CSV)
signal = df['Count'].values

# Aplicarea transformatei Fourier
N = len(signal)
fourier_transform = np.fft.fft(signal)
# fftfrq - obtine frecventele corespunzatoare la coeficientii din fourier_transform
# N - lungimea semnalului, d= intervalul dintre esantioane
frequencies = np.fft.fftfreq(N, d=1 / sampling_frequency)

# Identificarea frecvenței maxime
# se gaseste indexul coef cu cea mai mare magnitudine
max_frequency_index = np.argmax(np.abs(fourier_transform))
# se obtine frecventa corespunzatoare indexului gasit = > frecventa maxima din semnal
max_frequency = np.abs(frequencies[max_frequency_index])

print(f"Frecvența maximă în semnal: {max_frequency} Hz")

# Eliminarea componentei continue (valoarea medie) din semnal
signal_without_mean = signal - np.mean(signal)

# Aplicarea transformatei Fourier pe semnalul fără valoarea medie
fourier_transform = np.fft.fft(signal_without_mean)
frequencies = np.fft.fftfreq(N, d=1 / sampling_frequency)

# Identificarea frecvenței maxime
max_frequency_index = np.argmax(np.abs(fourier_transform))
max_frequency = np.abs(frequencies[max_frequency_index])

print(f"Frecvența maximă în semnal (fără componenta continuă): {max_frequency} Hz")

# d Afișarea modulului transformatei Fourier
plt.plot(frequencies, np.abs(fourier_transform))
plt.title('Modulul Transformatei Fourier')
plt.xlabel('Frecvență (Hz)')
plt.ylabel('Modul')
plt.savefig("ModululTransformatei.png")
plt.show()


# e Verificarea dacă semnalul are o componentă continuă
has_continuous_component = np.mean(signal) != 0

if has_continuous_component:
    print("Semnalul prezintă o componentă continuă.")
else:
    print("Semnalul nu prezintă o componentă continuă.")


# f
# Sortarea frecvențelor în ordine descrescătoare și identificarea primelor 4 frecvenț
# Se sortează coeficienții Transformatei Fourier în ordine descrescătoare și se identifică primele 4 frecvențe
# principale. Acestea sunt frecvențele cu magnitudinea cea mai mare în spectrul semnalului.
sorted_indices = np.argsort(np.abs(fourier_transform))[::-1]
top_frequencies = np.abs(frequencies[sorted_indices[:4]])


periods_in_seconds = 1 / top_frequencies
periods_in_days = 24 * 3600 / periods_in_seconds


print("Primele 4 frecvențe principale:")
for i, freq in enumerate(top_frequencies):
    print(f"Frecvența {i + 1}: {freq} Hz iar perioada {periods_in_days[i]}")

# g
# Alegerea esantionului de start pentru a incepe intr-o zi de luni
start_index = np.where(df['ID'].values > 1000)[0][0]

# Vizualizarea lunii de trafic
plt.plot(df['Datetime'].iloc[start_index:], df['Count'].iloc[start_index:])
plt.title('Luna de trafic')
plt.xlabel('Datetime')
plt.ylabel('Count')
plt.savefig("lunaTrafic.png")

# (i) Filtrarea semnalului
cutoff_frequency = 25  # Specificați o frecvență de tăiere
high_frequency_indices = np.abs(frequencies) > cutoff_frequency
fourier_transform[high_frequency_indices] = 0

# Afișarea modulului transformatei Fourier după filtrare
# Se specifică o frecvență de tăiere, iar toate frecvențele cu magnitudine mai mare decât această valoare sunt eliminate
# prin setarea coeficienților corespunzători la zero. Apoi, se afișează modulul Transformatei Fourier după filtrare.
# Acest proces poate evidenția doar componentele semnificative ale frecvențelor inferioare și poate elimina zgomotele
# de înaltă frecvență.
plt.plot(frequencies, np.abs(fourier_transform))
plt.title('Modulul Transformatei Fourier după filtrare')
plt.xlabel('Frecvență (Hz)')
plt.ylabel('Modul')
plt.savefig("TransformataDupaFiltrare.png")
plt.show()

