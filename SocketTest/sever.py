import socket 
import os

# Initialize Pygame mixer
from pygame import mixer
mixer.init()

host = '192.168.113.183'
port = 6767

# Mở socket ở sever 
sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#kết nối sever tới host/port
sever.bind((host, port))
print("HOST IN SEVER: " + host)

#sever bắt đầu lắng nghe trên port đó
sever.listen(1)
print("Server listening on port", port)

#chấp nhận yêu cầu kết nối từ client tới sever
client, address = sever.accept()

# Function to send audio data
def send_audio(filename):
    try:
        # Mở file audio
        with open(filename, 'rb') as file:
            
            # Đọc dữ liệu từ file 
            data = file.read()

            # gửi dữ liệu cho client
            client.sendall(data)

    except FileNotFoundError:
        # If the file is not found, inform the client
        client.send("File not found".encode())

#Nhận tên file do client gửi tới
filename = client.recv(1024)
print("FILENAME FROM SEVER: " + filename.decode())

project_directory = "E:\\Y3\\HK2-23_24\\MNM\\BT\\HarmonyHub\\SocketTest\\resource\\"
audio_path = os.path.join(project_directory, filename)

# Send audio data to the client
send_audio(audio_path)

client.close()

