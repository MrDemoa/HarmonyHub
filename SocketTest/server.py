import socket 
import os
import sys
import threading
import json
import time
import mysql.connector

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import date
from DAL.ConnectDB import ConnectSQL
from DTO.TrackDTO import TrackDTO
from DTO.UserDTO import UserDTO
from DTO.PlayListDTO import PlayListDTO
from DTO.PLDetailDTO import PLDetailDTO
from BLL.TrackBLL import TrackBLL
from BLL.AlbumBLL import AlbumBLL
from BLL.ArtistBLL import ArtistBLL
from BLL.PlayListBLL import PlayListBLL
from BLL.UserBLL import UserBLL
from BLL.PLDetailBLL import PLDetailBLL

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
        self.con = ConnectSQL.connect_mysql()
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
        if ("LOGIN" in signal):
            signal, username, password = signal.split("|")
            self.sendDataUser(client, username, password)
        elif ("RESET_PASSWORD" in signal):
            signal, username, new_password = signal.split("|")
            self.resetPassword(client, username, new_password)
        elif ("REGISTER" in signal):
            signal, username, email, password = signal.split("|")
            self.Register(client, userid, username, email, password)
        elif (signal == "DATA_PLAYLIST_USERID"):
            self.sendDataPlaylistWithUserID(client)
        elif (signal == "DATA_TRACK"):
            self.sendDataTrack(client)
        elif (signal == "DATA_ALBUM"):
            self.sendDataAlbum(client)
        elif (signal == "DATA_TRACK_ALBUM"):
            self.sendDataTrackInAlbum(client)
        elif (signal == "DATA_ARTIST"):
            self.sendDataArtist(client)
        elif (signal == "DATA_TRACK_ARTIST"):
            self.senDataTrackOfArtist(client)
        elif (signal == "PLAY_SONG_"):
            self.sendAudio(client, address)
        elif ("ADD_PLAYLIST" in signal):
            signal, playlistID, userID, title, creationdate = signal.split("|")
            self.addPlayList(playlistID, userID, title, creationdate)
        elif ("DELETE_PLAYLIST" in signal):
            signal, playlistID = signal.split("|")
            self.deletePlayList(playlistID)
        elif (signal == "ADD_TRACK_PLAYLIST"):
            self.insertTrackToPlayList(client)
        elif (signal == "DELETE_TRACK_PLAYLIST"):
            self.deleteTrackInPlayList(client)
        elif (signal == "GET_USERNAME_USERID"):
            self.sendDataUserNameByUserID(client)
    # def send_music(self, client, address):
    #     # Khởi tạo thread để nhận dữ liệu từ client
    #     self.receive_thread = threading.Thread(target=self.receive, args=(client, address))
    #     self.receive_thread.start()

    # def start_receive_thread_data(self, client):
    #     # Khởi tạo thread để nhận dữ liệu từ client
    #     self.receive_thread = threading.Thread(target=self.sendDataTrack, args=(client,))
    #     self.receive_thread.start()
    #========================================================================================

    def get_audio_file_path(self, track_name):
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

    # Gui du lieu album
    def sendDataAlbum(self, client):
        print("DANG GUI DU LIEU ALBUM!!!")
        data_album = AlbumBLL.getAllData(self) #lấy dữ liệu track từ DB
        print("DATA ALBUM: ", data_album)
        def tuple_to_dict(tpl):
            return {
                'albumID': tpl[0],
                'title': tpl[1],
                'artistID': tpl[2],
                'genre': tpl[3],
                'releasedate': tpl[4].strftime("%Y-%m-%d")
            }

        #Convert to JSON string using map and dumps
        json_string = json.dumps(list(map(tuple_to_dict, data_album)))
 
        client.send(json_string.encode())

    # Gui du lieu track cua mot album
    def sendDataTrackInAlbum(self, client):
        print("DANG GUI DU LIEU ARTIST!!!")
        albumID = client.recv(1024).decode()

        data_track_album = AlbumBLL.getTracksFromAlbumID(self, albumID) #lấy dữ liệu track từ DB

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
        json_string = json.dumps(list(map(tuple_to_dict, data_track_album)))
 
        client.send(json_string.encode())

    # Gui du lieu artist
    def sendDataArtist(self, client):
        print("DANG GUI DU LIEU ARTIST!!!")
        data_artist = ArtistBLL.getAllData(self) #lấy dữ liệu track từ DB

        def tuple_to_dict(tpl):
            return {
                'artistID': tpl[0],
                'name': tpl[1],
                'genre': tpl[2]
            }

        #Convert to JSON string using map and dumps
        json_string = json.dumps(list(map(tuple_to_dict, data_artist)))
 
        client.send(json_string.encode())

    # Gui du lieu track cua mot artist
    def sendDataTrackOfArtist(self, client):
        print("DANG GUI DU LIEU ARTIST!!!")
        artistID = client.recv(1024).decode()

        data_track_artist = ArtistBLL.getTracksFromArtistID(self, artistID) #lấy dữ liệu track từ DB

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
        json_string = json.dumps(list(map(tuple_to_dict, data_track_artist)))
 
        client.send(json_string.encode())


    # Gui du lieu kiem tra dang nhap
    def sendDataUser(self, client, username, password):
        checkLogin = str(UserBLL.checkUsernameAndPass(self, username, password)) #lấy dữ liệu track từ DB
        userID = str(UserBLL.getUserIDByUsername(self, username))
        print("CHECK LOGIN: ", checkLogin)
        print("USER ID: ", userID)
        message = checkLogin + "|" + userID 
        client.sendall(message.encode())
    
    def sendDataUserNameByUserID(self, client):
        userID = client.recv(1024).decode()
        username = str(UserBLL.getUserNameByUserId(self, userID))
        print("USERNAME: ", username)
        client.sendall(username.encode())    

    # Gui du lieu kiem tra dang nhap
    def resetPassword(self, client, username, new_password):
        print("DANG GUI DU LIEU USER!!!")
        # username = client.recv(1024).decode()
        # new_password = client.recv(1024).decode()
        user = UserBLL.checkUsername(self, username) #lấy dữ liệu track từ DB

        if user:
            UserBLL.resetPassWord(self, username, new_password)
            flag = True
            client.send(bytes([flag]))
        else:
            client.sendall("Username is Wrong!!!".encode())
            flag = False
            client.send(bytes([flag]))


    def Register(self, username, email, password):
        new_user = UserDTO()
        new_user.userID = UserBLL.generateUserID(self)
        new_user.username = username
        new_user.email = email
        new_user.password = password

        username = UserBLL.insert(self, new_user)

    def addPlayList(self, playlistID, userID, title, creationdate):
        pl = PlayListDTO()
        pl.playplistID = playlistID
        pl.userID = userID
        pl.title = title
        pl.createiondate = creationdate

        PlayListBLL.insert(self, pl) 
        
    def deletePlayList(self, playlistID):
        PlayListBLL.insert(self, playlistID) 

    # Gui du lieu album
    def sendDataPlaylistWithUserID(self, client):
        userID = client.recv(1024).decode()

        data_playlist = AlbumBLL.getDataPlaylistFromUserID(self, userID) #lấy dữ liệu track từ DB

        def tuple_to_dict(tpl):
            return {
                'playlistID': tpl[0],
                'title': tpl[2],
                'creationdate': tpl[3]
            }

        #Convert to JSON string using map and dumps
        json_string = json.dumps(list(map(tuple_to_dict, data_playlist)))
 
        client.send(json_string.encode())

    def sendDataTrackInPlaylist(self, client):
        playlistID = client.recv(1024).decode()

        data_track_playlist = ArtistBLL.getTracksFromPlaylistID(self, playlistID) #lấy dữ liệu track từ DB

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
        json_string = json.dumps(list(map(tuple_to_dict, data_track_playlist)))
 
        client.send(json_string.encode())

    def insertTrackToPlayList(self, client):

        detail = PLDetailDTO()
        detail.PlayListID = client.recv(1024).decode()
        detail.userID = client.recv(1024).decode()
        detail.TrackID = client.recv(1024).decode()

        PLDetailBLL.insertTracktoPlayList(self, detail) #lấy dữ liệu track từ DB

    def deleteTrackInPlayList(self, client):

        TrackID = client.recv(1024).decode()

        flag = PLDetailBLL.insertTracktoPlayList(self, TrackID) #lấy dữ liệu track từ DB
        
        client.send(bytes([flag]))

    def stop_server(self):
        try:
            self.server_socket.close()
            print("Server stopped")
        except Exception as e:
            print(f"Error stopping server: {e}")



    
    



