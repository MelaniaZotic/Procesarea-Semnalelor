import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile # folosit pentru citire fisierelor audio

# (a) Citirea semnalului audio dintr-un fișier
# wavfile.read returnează frecvența de eșantionare (fs) și datele audio (audio_data) din fișierul specificat.
fs, audio_data = wavfile.read('vocal_recording.wav')

# (b) Gruparea valorilor semnalului
group_size = int(0.01 * fs)  # Grupăm 1% din valorile semnalului
overlap = int(group_size / 2)  # Suprapunere de 50%

# (c) Calculul FFT pentru fiecare grup
# Se iterează prin semnal cu o fereastră glisantă și se aplică FFT pe fiecare grup.
# Rezultatele FFT sunt adăugate la lista spectrogram.
spectrogram = []
for i in range(0, len(audio_data) - group_size, overlap):
    group = audio_data[i:i + group_size]
    fft_result = np.abs(np.fft.fft(group))
    spectrogram.append(fft_result)

# (d) Construirea matricei
# Lista rezultatelor FFT este transformată într-o matrice folosind np.column_stack
spectrogram_matrix = np.column_stack(spectrogram)

# (e) Afișarea spectrogramei
plt.imshow(spectrogram_matrix, aspect='auto', cmap='viridis')
plt.title('Spectrograma Semnalului Audio')
plt.xlabel('Frecvență')
plt.ylabel('Timp')
plt.colorbar(label='Amplitudine')
plt.savefig("ex6.png")
plt.show()

