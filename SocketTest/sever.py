import socket 
import os
from zeroconf import ServiceInfo, Zeroconf
# Initialize Pygame mixer
from pygame import mixer
mixer.init()



def get_wifi_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

host_ip = get_wifi_ip()
port = 6767
info = ServiceInfo(
    "_http._tcp.local.",
    "My Service._http._tcp.local.",
    addresses=[socket.inet_aton(host_ip)],  # Replace with server's IP
    port=port,  # Replace with server's port
    properties={'property_name': 'property_value'},
    server="my_service.local.",
)
zeroconf = Zeroconf()
print("Registration of a service...")
zeroconf.register_service(info)
# Mở socket ở sever 
sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#kết nối sever tới host/port
sever.bind((host_ip, port))
print("HOST IN SEVER: " + host_ip)

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
try:
    filename = client.recv(1024).decode()
except ConnectionResetError:
    print("Kết nối bị đóng bởi máy chủ.")
print("FILENAME FROM SEVER: " + filename)

project_directory = os.path.abspath(os.path.dirname(__file__))
current_directory = os.path.join(project_directory, "resource\\SongList")
audio_path = os.path.join(current_directory, filename)

# Send audio data to the client
send_audio(audio_path)

client.close()

