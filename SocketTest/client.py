# fileclient.py

import socket 
import os
import time
from pygame import mixer

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

play_audio(temp_file_path)
time.sleep(300)
