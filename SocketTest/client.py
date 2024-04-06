# fileclient.py

import socket 
import os
import time
from pygame import mixer
from pydub import AudioSegment
#
mixer.init()

# Function to play audio
def play_audio(data):
    print("ĐANG GỌI HÀM PLAY AUDIO")
    mixer.music.load(data)
    mixer.music.set_volume(0.7) 
    mixer.music.play()


#Tạo socket ở client
client = socket.socket()

#Tạo kết nối với sever
client.connect(("localhost", 6767)) #lắng nghe ở cổng 6767

#Nhập vào tên file 
# Xác định đường dẫn cho file audio trong thư mục của project
#project_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = "E:\\Y3\\HK2-23_24\\MNM\\BT\\HarmonyHub\\SocketTest\\resource\\"
filename = project_directory + input("Enter a filename ")

#Gửi tên file cho server
client.send(filename.encode())

# Nhận dữ liệu từ server và lưu vào file audio
data = b''
while True:
    chunk = client.recv(1024)
    if not chunk:
        break
    data += chunk

client.close()

# Tạo một file tạm thời để lưu dữ liệu âm thanh từ máy chủ
temp_file_path = os.path.join(project_directory, "temp_audio.mp3")
with open(temp_file_path, 'wb') as temp_file:
    temp_file.write(data)

# Chuyển mp3 sang wav
def convert_mp3_to_wav(mp3_file, wav_file):
    # Load file MP3
    audio = AudioSegment.from_mp3(mp3_file)
    # Chuyển đổi sang WAV và lưu lại
    audio.export(wav_file, format="wav")

wav_file = "output.wav"
play_audio(temp_file_path, wav_file)
time.sleep(300)
