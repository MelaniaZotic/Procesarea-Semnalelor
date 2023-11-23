from networkx.drawing.tests.test_pylab import plt
from scipy.signal import butter, filtfilt

# (j) Eliminarea unui instrument specific
from skimage.metrics import peak_signal_noise_ratio

from Lab5.ex1 import signal, df, sampling_frequency

instrument_frequency = 500  # Specificați frecvența caracteristică a instrumentului
cutoff_frequency = 50  # Specificați o frecvență de tăiere pentru filtrul trece-jos

# Proiectarea unui filtru trece-jos
b, a = butter(N=6, Wn=cutoff_frequency / (0.5 * sampling_frequency), btype='low')

# Filtrarea semnalului audio
filtered_signal = filtfilt(b, a, signal)

# Afișarea semnalului audio original și a celui filtrat
plt.figure(figsize=(10, 6))
plt.plot(df['Datetime'], signal, label='Semnal original')
plt.plot(df['Datetime'], filtered_signal, label='Semnal filtrat')
plt.title('Eliminarea unui instrument specific')
plt.xlabel('Datetime')
plt.ylabel('Amplitudine')
plt.legend()
plt.savefig("SemnalFiltrat.png")
plt.show()

# Calculul raportului SNR înainte și după eliminare
snr_before_elimination = peak_signal_noise_ratio(signal, signal + np.random.normal(scale=0.5, size=len(signal)))
snr_after_elimination = peak_signal_noise_ratio(signal, filtered_signal)

print(f"Raport SNR înainte de eliminare: {snr_before_elimination:.2f} dB")
print(f"Raport SNR după eliminare: {snr_after_elimination:.2f} dB")