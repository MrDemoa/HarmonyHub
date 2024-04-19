import socket 
import os
import threading
import mysql.connector
# Initialize Pygame mixer
from pygame import mixer
mixer.init()
class Server:
    def __init__(self):
        #self.host_ip = self.get_wifi_ip()
        self.host_ip = "localhost"
        self.port = 6767
 
        # Mở socket ở sever 
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        #kết nối sever tới host/port
        self.server_socket.bind((self.host_ip, self.port))
        print("HOST IN SEVER: " + self.host_ip)

        #Lưu trữ danh sách các client và nicknames của họ
        self.clients = []
        self.nicknames = []
        
        #sever bắt đầu lắng nghe trên port đó
        self.server_socket.listen(5)
        print("Server listening on port", self.port)
        # Start the receive function in a separate thread to handle client connections
        self.receive_thread = threading.Thread(target=self.receive)
        self.receive_thread.start()
    def get_audio_file_path(self,track_name):
        # Directory where audio files are stored
        project_directory = os.getcwd()
        current_directory = os.path.join(project_directory, "SocketTest\\resource\\SongList")
        audio_directory = os.path.join(current_directory, filename)
        
        # Iterate through files in the audio directory
        for filename in os.listdir(audio_directory):
            # Check if the filename matches the track name
            if filename.startswith(track_name) and filename.endswith(".mp3"):
                # If found, return the full file path
                return os.path.join(audio_directory, filename)
        
        # If no matching file found, return None
        return None
    def disconnect(self,client):
        if client in self.clients:
            self.clients.remove(client)
            index = self.nicknames.index(client)
            nickname = self.nicknames[index]
            self.broadcast(f'{nickname} left the chat!'.encode('utf-8'))
            self.nicknames.remove(nickname)
            client.close()
            return True
        return False
    # Function to send audio data
    def send_audio(self,client,filename):
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

    def broadcast(self,message):
        for client in self.clients:
            client.send(message)
            
    def handle(self,client):
        while True:
            try:
                #Nhận dữ liệu từ client
                message = client.recv(1024).decode()
                #Gửi dữ liệu đến tất cả các client
                self.broadcast(message)
            except ConnectionAbortedError:
                print("Connection was aborted")
                break
            except :
                #Nếu có lỗi, xóa và đóng kết nối với client
                if client in self.clients:
                    self.clients.remove(client)
                    index = self.nicknames.index(client)
                    nickname = self.nicknames[index]
                    self.broadcast(f'{nickname} left the chat!'.encode('utf-8'))
                    self.nicknames.remove(nickname)
                break
    def receive(self):
        while True:
            client, address = self.server_socket.accept()
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
            self.nicknames.append(nickname)
            print(f"Nickname of the client is {nickname}")
            self.broadcast(f"{nickname} joined the chat!".encode('utf-8'))
            client.send('Connected to the server!'.encode('utf-8'))
            
            
            #Nhận tên file do client gửi tới
            filename = client.recv(1024).decode()
            print("FILENAME FROM SEVER: " + filename)

            # project_directory = os.getcwd()
            # current_directory = os.path.join(project_directory, "SocketTest\\resource\\SongList")
            # audio_path = os.path.join(current_directory, filename)
            # print("AUDIO PATH: " + audio_path)

            # # Send audio data to the client
            # send_audio(client,audio_path)
            # print("Audio data sent to the client")
            # thread=threading.Thread(target=handle,args=(client,))
            # thread.start()
            audio_path = self.get_audio_file_path(filename)
            print("AUDIO PATH: " + audio_path)

            if audio_path:
                self.send_audio(client, audio_path)
                print("Audio data sent to the client")
            else:
                print("Track not found")
                client.send("Track not found".encode())
    def get_wifi_ip(self):
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
    
server = Server()
    

    
    



