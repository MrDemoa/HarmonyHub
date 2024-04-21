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
        self.getDataTrackFromServer()
    
    def sendNameOfSongAndPlay(self, id):
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
            # Receive the size of the file from the server
            # print("ĐANG Ở ĐÂY")
            # file_size = int(self.client_socket.recv(1024).decode())
            # print("File size: ", file_size)
            # # Receive data from server and save it to an audio file
            # data = b''
            # received_size = 0
            # while received_size < file_size:
            #     chunk = self.client_socket.recv(1024)
            #     data += chunk
            #     received_size += len(chunk)


            # Write the received data to a temporary audio file
            # project_directory = os.path.abspath(os.path.dirname(__file__))
            # current_directory = os.path.join(project_directory, "resource")               
            # temp_file_path = os.path.join(current_directory, "temp_audio.mp3")
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

    def receive(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                self.song_listbox.insert(self.window.END, message)
            except:
                print('An error occurred!')
                self.client_socket.close()
                break 


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
            
            return record

    # Function to play audio
    def play_audio(self,data):
            print("ĐANG GỌI HÀM PLAY AUDIO")
            mixer.music.load(data)
            mixer.music.set_volume(0.1) 
            mixer.music.play()
            while mixer.music.get_busy():
                pygame.time.Clock().tick(10)

client = ClientListener() #mở client
#client.getDataFromServer()

