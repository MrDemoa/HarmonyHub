import socket 
import os
import threading

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
# info = ServiceInfo(
#     "_http._tcp.local.",
#     "My Service._http._tcp.local.",
#     addresses=[socket.inet_aton(host_ip)],  # Replace with server's IP
#     port=port,  # Replace with server's port
#     properties={'property_name': 'property_value'},
#     server="my_service.local.",
# )
# zeroconf = Zeroconf()
# print("Registration of a service...")
# zeroconf.register_service(info)

# Mở socket ở sever 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Create a UDP socket
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# # Broadcast the server's IP address and port
# message = f"{host_ip}:{port}".encode()
# server_socket.sendto(message, ('<broadcast>', 6767))
#kết nối sever tới host/port
server_socket.bind((host_ip, port))
print("HOST IN SEVER: " + host_ip)



# #chấp nhận yêu cầu kết nối từ client tới sever
# client, address = sever.accept()

#Lưu trữ danh sách các client và nicknames của họ
clients = []
nicknames = []
def disconnect(client):
    if client in clients:
        clients.remove(client)
        index = nicknames.index(client)
        nickname = nicknames[index]
        broadcast(f'{nickname} left the chat!'.encode('utf-8'))
        nicknames.remove(nickname)
        client.close()
        return True
    return False
# Function to send audio data
def send_audio(client,filename):
    try:
        # Mở file audio
        with open(filename, 'rb') as file:
            file_size = os.path.getsize(filename)
            client.send(str(file_size).encode())
            
            while True:
                # Đọc dữ liệu từ file
                data = file.read(1024)
                if not data:
                    break
                # Gửi dữ liệu cho client
                client.sendall(data)

    except FileNotFoundError:
        # If the file is not found, inform the client
        client.send("File not found".encode())

def broadcast(message):
    for client in clients:
        client.send(message)
        
def handle(client):
    while True:
        try:
            #Nhận dữ liệu từ client
            message = client.recv(1024).decode()
            #Gửi dữ liệu đến tất cả các client
            broadcast(message)
        except ConnectionAbortedError:
            print("Connection was aborted")
            break
        except :
            #Nếu có lỗi, xóa và đóng kết nối với client
            if client in clients:
                clients.remove(client)
                index = nicknames.index(client)
                nickname = nicknames[index]
                broadcast(f'{nickname} left the chat!'.encode('utf-8'))
                nicknames.remove(nickname)
            break
def receive():
    while True:
        client, address = server_socket.accept()
        print(f"Connected with {str(address)}")
        client.send('NICK'.encode('utf-8'))
        # Wait for a response from the client
        response = client.recv(1024).decode('utf-8')
        if response != 'ACK':
            print("Handshake failed")
            client.close()
            continue
        try:
            nickname = client.recv(1024).decode('utf-8')
        except ConnectionResetError:
            print("Connection was reset")
            continue
        nicknames.append(nickname)
        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode('utf-8'))
        client.send('Connected to the server!'.encode('utf-8'))
        
        
        #Nhận tên file do client gửi tới
        filename = client.recv(1024).decode()
        print("FILENAME FROM SEVER: " + filename)

        project_directory = os.getcwd()
        current_directory = os.path.join(project_directory, "SocketTest\\resource\\SongList")
        audio_path = os.path.join(current_directory, filename)
        print("AUDIO PATH: " + audio_path)

        # Send audio data to the client
        send_audio(client,audio_path)
        print("Audio data sent to the client")
        thread=threading.Thread(target=handle,args=(client,))
        thread.start()
        
       
#sever bắt đầu lắng nghe trên port đó
server_socket.listen(5)
print("Server listening on port", port)

# Start the receive function in a separate thread to handle client connections
receive_thread = threading.Thread(target=receive)
receive_thread.start()

    
    

#     client.close()

