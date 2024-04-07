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


# #Tạo socket ở client
# client = socket.socket()

# #Tạo kết nối với sever
# client.connect(("192.168.3.115", 6767)) #lắng nghe ở cổng 6767

# Server address and port
SERVER_IP = "192.168.3.115"  # Replace with the IP of the server PC on your LAN
SERVER_PORT = 6767

# Connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, SERVER_PORT))


# #Nhập vào tên file 
# # Xác định đường dẫn cho file audio trong thư mục của project
# #project_directory = os.path.dirname(os.path.abspath(__file__))
# project_directory = "C:\\Users\\ACER\\Desktop\\File C\\HarmonyHub\\SocketTest\\resource\\"
# filename = project_directory + input("Enter a filename ")

# #Gửi tên file cho server
# client.send(filename.encode())

# Input filename from the user
filename = input("Enter the filename: ")
client.send(filename.encode())

# Nhận dữ liệu từ server và lưu vào file audio
data = b''
while True:
    chunk = client.recv(1024)
    if not chunk:
        break
    data += chunk

client.close()

# # Tạo một file tạm thời để lưu dữ liệu âm thanh từ máy chủ
# temp_file_path = os.path.join(project_directory, "temp_audio.mp3")
# with open(temp_file_path, 'wb') as temp_file:
#     temp_file.write(data)

# play_audio(temp_file_path)
# time.sleep(300)

# Write the received data to a temporary audio file
project_directory = "C:\\Users\\ACER\\Desktop\\File C\\HarmonyHub\\SocketTest\\resource\\"
temp_file_path = os.path.join(project_directory, "temp_audio.mp3")
with open(temp_file_path, 'wb') as temp_file:
    temp_file.write(data)

# Play the received audio
play_audio(temp_file_path)

# Wait for 5 minutes (300 seconds)
time.sleep(300)