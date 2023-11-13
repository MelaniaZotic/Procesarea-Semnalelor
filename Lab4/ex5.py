import sounddevice as sd
import librosa
import librosa.display
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

# Setările pentru înregistrare
duration = 5  # Durata înregistrării în secunde
sample_rate = 22050  # Rata de eșantionare

# Înregistrați sunetul
print("Începeți să vorbiți sau să cântați!")
audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
sd.wait()

# Salvați înregistrarea într-un fișier audio
file_path = "vocal_recording.wav"
sf.write(file_path, audio_data.flatten(), sample_rate)

# Încărcați înregistrarea audio utilizând Librosa
y, sr = librosa.load(file_path, sr=sample_rate)

# Afișați spectrograma
plt.figure(figsize=(10, 4))
librosa.display.specshow(librosa.amplitude_to_db(librosa.stft(y), ref=np.max), y_axis='log', x_axis='time')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrograma')
plt.savefig("ex5.png")
plt.show()