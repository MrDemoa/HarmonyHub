import socket 
import os
import sys
import threading
import json
import time
import mysql.connector

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import date
from DTO.TrackDTO import TrackDTO
from BLL.TrackBLL import TrackBLL

# Initialize Pygame mixer
from pygame import mixer


mixer.init()

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)

class Server:
    #========================================================================================
    ip = "localhost"
    port = 6767

    def __init__(self):
        # Khởi tạo socket của server
        self.host_ip = Server.ip
        self.port = Server.port
        # Bắt đầu lắng nghe các kết nối đến server
        self.runServer()

    def runServer(self):
        # Tạo socket của server
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Bind socket với host và port
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host_ip, self.port))
        print("HOST IN SEVER: " + self.host_ip)

        self.server_socket.listen(5)
        print("Server listening on port", self.port)

        while True:
            self.getSignal()
        
    def getSignal(self):
        # Chấp nhận kết nối từ client và khởi tạo xử lý
        print("Đang chờ kết nối: ")
        client, address = self.server_socket.accept()
        signal = client.recv(1024).decode("utf-8")
        print(signal)
        if (signal == "PLAY_SONG_"):
            self.sendAudio(client, address)
        elif (signal == "DATA_TRACK"):
            self.sendDataTrack(client)
        elif (signal == "DATA_ALBUM"):
            self.senDataAlbum(client)
        elif (signal == "DATA_TRACK_ALBUM"):
            self.senDataTrackInAlbum(client)
        elif (signal == "DATA_ARTIST"):
            self.senDataArtist(client)
        elif (signal == "DATA_TRACK_ARTIST"):
            self.senDataTrackOfArtist(client)

    # def send_music(self, client, address):
    #     # Khởi tạo thread để nhận dữ liệu từ client
    #     self.receive_thread = threading.Thread(target=self.receive, args=(client, address))
    #     self.receive_thread.start()

    # def start_receive_thread_data(self, client):
    #     # Khởi tạo thread để nhận dữ liệu từ client
    #     self.receive_thread = threading.Thread(target=self.sendDataTrack, args=(client,))
    #     self.receive_thread.start()
    #========================================================================================

    def get_audio_file_path(self,track_name):
        # Directory where audio files are stored
        project_directory = os.getcwd()
        current_directory = os.path.join(project_directory, "SocketTest\\resource\\SongList")
        
        
        # Iterate through files in the audio directory
        for filename in os.listdir(current_directory):
            # Check if the filename matches the track name
            if filename.startswith(track_name) and filename.endswith(".mp3"):
                # If found, return the full file path
                return os.path.join(current_directory, filename)
        
        # If no matching file found, return None
        return None


    # Function to send audio data
    def send_audio(self, client, filename):
        try:
            # Mở file audio
            with open(filename, 'rb') as file:
                # file_size = os.path.getsize(filename)
                # print("FILE SIZE:" + file_size)
                # client.send(str(file_size).encode())
                
                # with open(filename, "rb") as music_file:
                #     data = music_file.read(1024)
                #     while data:
                #         self.clientSocket.sendall(data)
                #         data = music_file.read(1024)

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
                if client:
                    self.remove(client)
                    index = self.nicknames.index(client)
                    nickname = self.nicknames[index]
                    self.broadcast(f'{nickname} left the chat!'.encode('utf-8'))
                    self.nicknames.remove(nickname)
                break

    def sendAudio(self, client, address):
            print(f"Connected with {str(address)}")
            #Nhận tên file do client gửi tới
            filename = client.recv(1024).decode() + ".mp3"
            print("FILENAME FROM SEVER:" + filename)


            audio_path = self.get_audio_file_path(filename)
            print("AUDIO PATH: " + audio_path)

            if audio_path:
                try:
                    # Mở file audio
                    with open(audio_path, 'rb') as file:
                        # file_size = os.path.getsize(filename)
                        # print("FILE SIZE:" + file_size)
                        # client.send(str(file_size).encode())
                        
                        # with open(filename, "rb") as music_file:
                        #     data = music_file.read(1024)
                        #     while data:
                        #         self.clientSocket.sendall(data)
                        #         data = music_file.read(1024)

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
    
    # hàm lấy dữ liệu track từ db
    def getDataTrack(self):
        return TrackBLL.getAllData(self)

    def sendDataTrack(self, client):
        print("DANG GUI DU LIEU TRACK!!!")
        data_track = TrackBLL.getAllData(self) #lấy dữ liệu track từ DB

        def tuple_to_dict(tpl):
            return {
                'trackID': tpl[0],
                'title': tpl[1],
                'artistID': tpl[2],
                'albumID': tpl[3],
                'duration': tpl[4],
                'releasedate': tpl[5].strftime("%Y-%m-%d")
            }

        #Convert to JSON string using map and dumps
        json_string = json.dumps(list(map(tuple_to_dict, data_track)))
 
        client.send(json_string.encode())
    def stop_server(self):
        try:
            self.server_socket.close()
            print("Server stopped")
        except Exception as e:
            print(f"Error stopping server: {e}")

# server = Server()



    
    



