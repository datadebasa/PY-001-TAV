import cv2
import os
import requests
import numpy as np
from io import BytesIO
from PIL import Image
from moviepy.editor import VideoFileClip, AudioFileClip

# Daftar URL gambar
image_urls = [
    "https://assets-a2.kompasiana.com/items/album/2023/04/23/screenshot-2023-04-23-12-03-10-44-965bbf4d18d205f782c6b8409c5773a4-6444bc4508a8b56c9e546312.jpg?t=o&v=500",
    # Tambahkan URL gambar lainnya di sini
]

# Nama file video sementara tanpa audio
temp_video_name = "temp_output_video.avi"
# Nama file video final dengan audio
final_video_name = "Sodikin-kasihan-sekali.mp4"
# Path file audio
audio_path = "manual.mp3"

# Mendownload gambar dari URL dan menyimpannya dalam list
images = []
for url in image_urls:
    response = requests.get(url)
    img = Image.open(BytesIO(response.content)).convert("RGB")  # Konversi gambar ke RGB
    images.append(cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR))

# Mendapatkan dimensi dari gambar pertama untuk mengatur ukuran video
height, width, layers = images[0].shape

# Menggabungkan video dengan audio menggunakan moviepy untuk mendapatkan durasi audio
audio_clip = AudioFileClip(audio_path)
audio_duration = audio_clip.duration

# Menentukan frame rate agar video sesuai dengan durasi audio
frame_rate = audio_duration

# Menentukan format video output, codec, dan frame rate
video = cv2.VideoWriter(
    temp_video_name, cv2.VideoWriter_fourcc(*"DIVX"), frame_rate, (width, height)
)

for image in images:
    video.write(image)

cv2.destroyAllWindows()
video.release()

# Menggabungkan video dengan audio menggunakan moviepy
video_clip = VideoFileClip(temp_video_name)
video_clip = video_clip.set_audio(audio_clip)

# Memastikan durasi video dan audio sama
video_clip = video_clip.set_duration(audio_duration)

# Menyimpan video final
video_clip.write_videofile(final_video_name, codec="libx264")

# Menghapus file video sementara
os.remove(temp_video_name)

# end
