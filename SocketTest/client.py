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
from mutagen.mp3 import MP3
mixer.init()
# server_ip='192.168.3.115'
# port=6767
class ClientListener:
    
    def __init__(self):
        self.host_ip = "localhost"
        self.port = 6767
        # Add a state variable to keep track of whether the audio is muted
        self.is_muted = False
        self.temp_audio_file = None
        self.isPlayThisSong = False
        self.pause_state = False
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
            print("Song received and stored in self.temp_audio_file")            
            file_name = "received_song.mp3"
            with open(file_name, 'wb') as f:
                temp_audio_file.seek(0)
                f.write(temp_audio_file.read())
           
            
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
            self.isPlayThisSong = True
            mixer.music.load(data)
            mixer.music.set_volume(20) 
            mixer.music.play()
            while mixer.music.get_busy():
                pygame.time.Clock().tick(10)
    def get_music_length(self):    
        filename = 'received_song.mp3'
        # Get the length of the music
        audio = MP3(filename)
        music_length = audio.info.length
        
        return music_length
    def convert_time_to_string(self):
        # Convert the length to minutes and seconds
        minutes, seconds = divmod(self.get_music_length(), 60)
        # Format the length as a string
        music_length_str = f"{int(minutes)}:{int(seconds):02d}"
    
        return music_length_str
    def set_volume(self, volume):
        mixer.music.set_volume(volume)
    def set_time(self, time):
        # Check if music is playing
        if mixer.music.get_busy():
            # Get the total length of the music
            music_length = self.get_music_length()
            # Calculate the new position in the music
            new_position = float(time) * music_length
            
            mixer.music.set_pos(new_position)
        else:
            print("Music isn't playing")
        

    # Function to pause audio
    def Pause_audio(self):
        self.pause_state = True
        mixer.music.pause()

    def isPaused(self):
        return self.pause_state

    # Function to unpause audio:
    def Unpause_audio(self):
        self.pause_state = False
        mixer.music.unpause()

    def isPlaying(self):
        return self.isPlayThisSong

    def set_volume(self, volume):
        mixer.music.set_volume(volume)

    def mute_volume(self):
        if self.is_muted:
            # If the audio is currently muted, unmute it
            mixer.music.set_volume(self.previous_volume)
            self.is_muted = False
        else:
            # If the audio is currently unmuted, mute it
            self.previous_volume = mixer.music.get_volume()
            mixer.music.set_volume(0)
            self.is_muted = True

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
    def getDataPlayListFromServer(self, userID):
            try:
                self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # gửi yêu cầu connect
                self.client_socket.connect((self.host_ip, self.port)) 
                signal = "DATA_PLAYLIST_USERID" 
                self.client_socket.sendall(signal.encode())

            except socket.timeout as e:
                print("A timeout error occurred while trying to connect to the server:", str(e))
            except OSError as e:
                print("An error occurred while trying to receive data:", str(e))
                return
            except Exception as e:
                print("An error occurred while trying to connect to the server:", str(e))
                return 
            
            #Gửi userID cho server
            print("sending userID to server",userID)
            self.client_socket.sendall(userID.encode())

            # Nhận dữ liệu từ server
            print("NHẬN DỮ LIỆU TỪ SEVER!!!")
            received_data = self.client_socket.recv(4096)
            # decode dữ liệu
            json_data_track = received_data.decode()
            print(f"Received data: {json_data_track}")
            

            # chuyển đổi dữ liệu từ dạng JSON thành danh sách từ điển
            data_track = json.loads(json_data_track)
            
            # Print the received data
            print("Received data track:")
            for record in data_track:
                print(record)
            
            return data_track
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
    def getUserNameByUserID(self, userID):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # gửi yêu cầu connect
            self.client_socket.connect((self.host_ip, self.port)) 
            signal = "GET_USERNAME_USERID" 
            self.client_socket.sendall(signal.encode())

        except socket.timeout as e:
            print("TIMEOUT ERROR:", str(e))
        except OSError as e:
            print("FAILED TO RECEIVE DATA:", str(e))
            return
        except Exception as e:
            print("ERROR:", str(e))
            return 
        print("userID:", userID)
        self.client_socket.sendall(userID.encode())

        # Nhận dữ liệu từ server
        print("NHẬN DỮ LIỆU TỪ SEVER!!!")
        received_data = self.client_socket.recv(4096)

        # decode dữ liệu
        username = received_data.decode()
    
        return username
    def checkLogin(self, username, password):
        # Assign a default value to Notification_Server
        Notification_Server = ""
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
        # Check the length of the sequence
        if "|" in Notification_Server:
            print("Notification_Server:", Notification_Server)
            Notification, userID = Notification_Server.split("|")
            return Notification, userID
        else:
            return False, None
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
    
    def Register(self, UserName, Email, PassWord):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # gửi yêu cầu connect
            self.client_socket.connect((self.host_ip, self.port)) 
            signal = "REGISTER" 
            message = signal + "|" + UserName + "|" + Email + "|" + PassWord
            self.client_socket.sendall(message.encode())
            msg = self.client_socket.recv(1024).decode("utf-8")

        except socket.timeout as e:
            print("TIMEOUT ERROR:", str(e))
        except OSError as e:
            print("FAILED TO RECEIVE DATA:", str(e))
            return
        except Exception as e:
            print("ERROR:", str(e))
            return
        print("msg:", msg)
        return msg

    def addTrackToPlayList(self, PlayListID, UserID, trackID):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # gửi yêu cầu connect
            self.client_socket.connect((self.host_ip, self.port)) 
            signal = "ADD_TRACK_PLAYLIST" 
            message = signal + "|" + PlayListID + "|" + UserID + "|" + trackID
            self.client_socket.sendall(message.encode())

        except socket.timeout as e:
            print("TIMEOUT ERROR:", str(e))
        except OSError as e:
            print("FAILED TO RECEIVE DATA:", str(e))
            return
        except Exception as e:
            print("ERROR:", str(e))
            return 


        
    def deleteTrackInPlayList(self, trackID):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # gửi yêu cầu connect
            self.client_socket.connect((self.host_ip, self.port)) 
            signal = "DELETE_TRACK_PLAYLIST" 
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
    
    def addPlayList(self, userID, title, creationdate):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # gửi yêu cầu connect
            self.client_socket.connect((self.host_ip, self.port)) 
            signal = "ADD_PLAYLIST"
            message = signal  + "|" + userID + "|" + title + "|" + creationdate
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
        
    def deletePlayList(self, playlistID):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # gửi yêu cầu connect
            self.client_socket.connect((self.host_ip, self.port)) 
            signal = "DELETE_PLAYLIST"
            message = signal  + "|" + playlistID 
            self.client_socket.sendall(message.encode())

        except socket.timeout as e:
            print("TIMEOUT ERROR:", str(e))
        except OSError as e:
            print("FAILED TO RECEIVE DATA:", str(e))
            return
        except Exception as e:
            print("ERROR:", str(e))
            return 
        
        Notification_Server = self.client_socket.recv(1024)

        Notification = bool(int.from_bytes(Notification_Server, byteorder='big'))

        return Notification
        
     

if __name__ == "__main__":
    client = ClientListener() #mở client
