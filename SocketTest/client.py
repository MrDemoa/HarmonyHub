# fileclient.py
import socket 
import os
import time
import json
import tempfile
import pygame
from pygame import mixer
from datetime import datetime
import threading

mixer.init()
# server_ip='192.168.3.115'
# port=6767
class ClientListener:
    
    def __init__(self):
        self.host_ip = "localhost"
        self.port = 6767

        # response = self.client_socket.recv(1024).decode()
        # print("Received response from server:", response)
        # make a handshake with the server
        # self.sendNameOfSongAndPlay('T01')
        # time.sleep(2)
        # self.getDataTrackFromServer()
    def sendNameOfSongAndPlay(self, id):
        threading.Thread(target=self._sendNameOfSongAndPlay, args=(id,)).start()
    def _sendNameOfSongAndPlay(self, id):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # gửi yêu cầu connect
            self.client_socket.connect((self.host_ip, self.port))
            signal = "PLAY_SONG_" 
            self.client_socket.sendall(signal.encode())

        except socket.timeout as e:
            print("A timeout error occurred while trying to connect to the server:", str(e))
        except OSError as e:
            print("An error occurred while trying to receive data:", str(e))
            return
        except Exception as e:
            print("An error occurred while trying to connect to the server:", str(e))
            return 
        
        try:
            if isinstance(id, str) and id:
                print("ID:",id)
                print(type(id))
                self.client_socket.sendall(id.encode())
            
            self.receiveSong()          
        except Exception as e:
            # If an error occurs (like the server disconnecting), print the error and break the loop
            print("Error at send filename point:", str(e))


    def receiveSong(self):

            temp_audio_file = tempfile.SpooledTemporaryFile(max_size=10000000)  # Adjust max_size as needed

            while True:
                data = self.client_socket.recv(1024)
                if not data:
                    break
                temp_audio_file.write(data)
                        

            temp_audio_file.seek(0)
            #Play the received audio
            self.play_audio(temp_audio_file)
            #time.sleep(200)
            # Load the temporary file as music

            # Wait for 5 minutes (300 seconds)
            # time_mp3 = file_size * 8 /(128 * 1000)
            # print(time_mp3)
            # time.sleep(time_mp3)

    # Function to play audio
    def play_audio(self,data):
            print("ĐANG GỌI HÀM PLAY AUDIO")
            mixer.music.load(data)
            mixer.music.set_volume(0.1) 
            mixer.music.play()
            while mixer.music.get_busy():
                pygame.time.Clock().tick(10)


    # Hàm nhận dữ liệu từ server
    def getDataTrackFromServer(self):
            try:
                self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # gửi yêu cầu connect
                self.client_socket.connect((self.host_ip, self.port)) 
                signal = "DATA_TRACK" 
                self.client_socket.sendall(signal.encode())

            except socket.timeout as e:
                print("A timeout error occurred while trying to connect to the server:", str(e))
            except OSError as e:
                print("An error occurred while trying to receive data:", str(e))
                return
            except Exception as e:
                print("An error occurred while trying to connect to the server:", str(e))
                return 


            # Nhận dữ liệu từ server
            print("NHẬN DỮ LIỆU TỪ SEVER!!!")
            received_data = self.client_socket.recv(4096)

            # decode dữ liệu
            json_data_track = received_data.decode()
            

            # chuyển đổi dữ liệu từ dạng JSON thành danh sách từ điển
            data_track = json.loads(json_data_track)
            
            # Print the received data
            print("Received data track:")
            for record in data_track:
                print(record)
            
            return data_track

    def getDataAlbumFromServer(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # gửi yêu cầu connect
            self.client_socket.connect((self.host_ip, self.port)) 
            signal = "DATA_ALBUM" 
            self.client_socket.sendall(signal.encode())

        except socket.timeout as e:
            print("TIMEOUT ERROR:", str(e))
        except OSError as e:
            print("FAILED TO RECEIVE DATA:", str(e))
            return
        except Exception as e:
            print("ERROR:", str(e))
            return 


        # Nhận dữ liệu từ server
        print("NHẬN DỮ LIỆU TỪ SEVER!!!")
        received_data = self.client_socket.recv(4096)

        # decode dữ liệu
        json_data_album = received_data.decode()
            
        # chuyển đổi dữ liệu từ dạng JSON thành danh sách từ điển
        data_album = json.loads(json_data_album)
            
        # Print the received data
        print("Received data album:")
        for record in data_album:
            print(record)
            
        return data_album
        
    def getDataTrackInAlbum(self, albumID):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # gửi yêu cầu connect
            self.client_socket.connect((self.host_ip, self.port)) 
            signal = "DATA_TRACK_ALBUM" 
            self.client_socket.sendall(signal.encode())

        except socket.timeout as e:
            print("TIMEOUT ERROR:", str(e))
        except OSError as e:
            print("FAILED TO RECEIVE DATA:", str(e))
            return
        except Exception as e:
            print("ERROR:", str(e))
            return 

        #Gửi albumID cho server
        self.client_socket.sendall(albumID.encode())

        # Nhận dữ liệu từ server
        print("NHẬN DỮ LIỆU TỪ SEVER!!!")
        received_data = self.client_socket.recv(4096)

        # decode dữ liệu
        track_in_album = received_data.decode()
            
        # chuyển đổi dữ liệu từ dạng JSON thành danh sách từ điển
        data = json.loads(track_in_album)
            
        # Print the received data
        print("Received data album:")
        for record in data:
            print(record)
            
        return record
        
    def getDataArtistFromServer(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # gửi yêu cầu connect
            self.client_socket.connect((self.host_ip, self.port)) 
            signal = "DATA_ARTIST" 
            self.client_socket.sendall(signal.encode())

        except socket.timeout as e:
            print("TIMEOUT ERROR:", str(e))
        except OSError as e:
            print("FAILED TO RECEIVE DATA:", str(e))
            return
        except Exception as e:
            print("ERROR:", str(e))
            return 


        # Nhận dữ liệu từ server
        print("NHẬN DỮ LIỆU TỪ SEVER!!!")
        received_data = self.client_socket.recv(4096)

        # decode dữ liệu
        json_data_artist = received_data.decode()
            
        # chuyển đổi dữ liệu từ dạng JSON thành danh sách từ điển
        data_artist = json.loads(json_data_artist)
            
        # Print the received data
        print("Received data artist:")
        for record in data_artist:
            print(record)
            
        return data_artist

    def getDataTrackOfArtist(self, artistID):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # gửi yêu cầu connect
            self.client_socket.connect((self.host_ip, self.port)) 
            signal = "RESET_PASSWORD" 
            self.client_socket.sendall(signal.encode())

        except socket.timeout as e:
            print("TIMEOUT ERROR:", str(e))
        except OSError as e:
            print("FAILED TO RECEIVE DATA:", str(e))
            return
        except Exception as e:
            print("ERROR:", str(e))
            return 

        #Gửi albumID cho server
        self.client_socket.sendall(artistID.encode())

        # Nhận dữ liệu từ server
        print("NHẬN DỮ LIỆU TỪ SEVER!!!")
        received_data = self.client_socket.recv(4096)

        # decode dữ liệu
        track_in_artist = received_data.decode()
            
        # chuyển đổi dữ liệu từ dạng JSON thành danh sách từ điển
        data = json.loads(track_in_artist)
            
        # Print the received data
        print("Received data artist:")
        for record in data:
            print(record)
            
        return data
    
    def checkLogin(self, username, password):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # gửi yêu cầu connect
            self.client_socket.connect((self.host_ip, self.port)) 
            signal = "LOGIN"
            message = signal + "|" + username + "|" + password 
            self.client_socket.sendall(message.encode())
            #self.client_socket.recv(1024).decode("utf-8")

        except socket.timeout as e:
            print("TIMEOUT ERROR:", str(e))
        except OSError as e:
            print("FAILED TO RECEIVE DATA:", str(e))
            return
        except Exception as e:
            print("ERROR:", str(e))
            return 
    

        Notification_Server = self.client_socket.recv(1024).decode()
        print("Notification_Server:", Notification_Server)
        Notification, userID = Notification_Server.split("|")

        return Notification, userID
    
    def resetPassword(self, username, new_password):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # gửi yêu cầu connect
            self.client_socket.connect((self.host_ip, self.port)) 
            signal = "RESET_PASSWORD" 
            message = signal + "|" + username + "|" + new_password 
            self.client_socket.sendall(message.encode())

        except socket.timeout as e:
            print("TIMEOUT ERROR:", str(e))
        except OSError as e:
            print("FAILED TO RECEIVE DATA:", str(e))
            return
        except Exception as e:
            print("ERROR:", str(e))
            return 
        
        # self.client_socket.sendall(username.encode())
        # self.client_socket.sendall(new_password.encode())

        # Thông báo thành công hoặc thất bại
        Notification_Server = self.client_socket.recv(1024)

        Notification = bool(int.from_bytes(Notification_Server, byteorder='big'))

        return Notification
    
    def addTrackToPlayList(self, PlayListID, UserID, trackID):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # gửi yêu cầu connect
            self.client_socket.connect((self.host_ip, self.port)) 
            signal = "ADD_TRACK_PLAYLIST" 
            self.client_socket.sendall(signal.encode())

        except socket.timeout as e:
            print("TIMEOUT ERROR:", str(e))
        except OSError as e:
            print("FAILED TO RECEIVE DATA:", str(e))
            return
        except Exception as e:
            print("ERROR:", str(e))
            return 

        self.client_socket.sendall(PlayListID.encode())
        self.client_socket.sendall(UserID.encode())
        self.client_socket.sendall(trackID.encode())

        
    def deleteTrackInPlayList(self, trackID):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # gửi yêu cầu connect
            self.client_socket.connect((self.host_ip, self.port)) 
            signal = "ADD_TRACK_PLAYLIST" 
            self.client_socket.sendall(signal.encode())

        except socket.timeout as e:
            print("TIMEOUT ERROR:", str(e))
        except OSError as e:
            print("FAILED TO RECEIVE DATA:", str(e))
            return
        except Exception as e:
            print("ERROR:", str(e))
            return 

        self.client_socket.sendall(trackID.encode())

        # Thông báo thành công hoặc thất bại
        Notification_Server = client.recv(1024)

        Notification = bool(int.from_bytes(Notification_Server, byteorder='big'))

        return Notification
    
    def getDataTrackOfArtist(self, artistID):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # gửi yêu cầu connect
            self.client_socket.connect((self.host_ip, self.port)) 
            signal = "DATA_PLAYLIST_USERID" 
            self.client_socket.sendall(signal.encode())

        except socket.timeout as e:
            print("TIMEOUT ERROR:", str(e))
        except OSError as e:
            print("FAILED TO RECEIVE DATA:", str(e))
            return
        except Exception as e:
            print("ERROR:", str(e))
            return 

        #Gửi albumID cho server
        self.client_socket.sendall(artistID.encode())

        # Nhận dữ liệu từ server
        print("NHẬN DỮ LIỆU TỪ SEVER!!!")
        received_data = self.client_socket.recv(4096)

        # decode dữ liệu
        track_in_artist = received_data.decode()
            
        # chuyển đổi dữ liệu từ dạng JSON thành danh sách từ điển
        data = json.loads(track_in_artist)
            
        # Print the received data
        print("Received data artist:")
        for record in data:
            print(record)
            
        return data
    
    def addPlayList(self, playlistID, userID, title, creationdate):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # gửi yêu cầu connect
            self.client_socket.connect((self.host_ip, self.port)) 
            signal = "ADD_PLAYLIST"
            message = signal + "|" + playlistID + "|" + userID + "|" + title + "|" + creationdate
            self.client_socket.sendall(message.encode())
            #self.client_socket.recv(1024).decode("utf-8")

        except socket.timeout as e:
            print("TIMEOUT ERROR:", str(e))
        except OSError as e:
            print("FAILED TO RECEIVE DATA:", str(e))
            return
        except Exception as e:
            print("ERROR:", str(e))
            return 
        
    def addPlayList(self, playlistID):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # gửi yêu cầu connect
            self.client_socket.connect((self.host_ip, self.port)) 
            signal = "ADD_PLAYLIST"
            message = signal + "|" + playlistID 
            self.client_socket.sendall(message.encode())
            #self.client_socket.recv(1024).decode("utf-8")

        except socket.timeout as e:
            print("TIMEOUT ERROR:", str(e))
        except OSError as e:
            print("FAILED TO RECEIVE DATA:", str(e))
            return
        except Exception as e:
            print("ERROR:", str(e))
            return 
     

if __name__ == "__main__":
    client = ClientListener() #mở client

