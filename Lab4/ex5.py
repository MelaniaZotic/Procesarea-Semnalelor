import librosa.display
import numpy as np
import matplotlib.pyplot as plt

# Calea către fișierul audio înregistrat
file_path = "vocal_recording.wav"

# Încărcați înregistrarea audio utilizând Librosa
y, sr = librosa.load(file_path, sr=None)

# Afișați spectrograma
plt.figure(figsize=(10, 4))
librosa.display.specshow(librosa.amplitude_to_db(librosa.stft(y), ref=np.max), y_axis='log', x_axis='time')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrograma')
plt.savefig("ex5.png")
plt.show()

# Spectrograma este o reprezentare vizuală a spectrului de frecvență al unui semnal audio în funcție de timp.
# Pe axa orizontală avem timpul, pe axa verticală avem frecvența, iar intensitatea culorilor indică magnitudinea
# spectrului la o anumită frecvență și timp
