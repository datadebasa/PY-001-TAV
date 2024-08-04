# Install necessary libraries
from gtts import gTTS
from pydub import AudioSegment

# Define the text to be converted to speech
text = """
Nama saya adalah Sodikin dari Universitas Teknokrat Indonesia, saya semester 8 dan saya masih mengerjakan skripsi, saya juga sudah mau masuk semester 9 :... Sedih sekali
"""
# Generate the speech
tts = gTTS(text, lang="id")
tts.save("manual.mp3")
