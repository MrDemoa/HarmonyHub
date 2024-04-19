# fileclient.py
import socket 
import os
import time
from pygame import mixer
import threading

mixer.init()
# server_ip='192.168.3.115'
# port=6767
class ClientListener:
    
    def __init__(self):
        self.host_ip = "192.168.3.115"
        self.port = 6767
        
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.host_ip, self.port))  
            response = self.client_socket.recv(1024).decode()
            print("Received response from server:", response)
            # make a handshake with the server
            self.client_socket.send("ACK".encode())
            # Send a nickname to the server
            self.client_socket.send("MrDemo".encode())
        except socket.timeout as e:
            print("A timeout error occurred while trying to connect to the server:", str(e))
        except OSError as e:
            print("An error occurred while trying to receive data:", str(e))
            return
        except Exception as e:
            print("An error occurred while trying to connect to the server:", str(e))
            return    
    
        
        
        while True:
            try:
                # Try to receive data from the server
                response = self.client_socket.recv(1024).decode()
                print("Received response from server:", response)
                # If the server sends an audio file, play it
                filename = input("Enter the filename: ")

                if filename:
                    self.client_socket.send(filename.encode())
                        
                    # Receive the size of the file from the server
                    file_size = int(self.client_socket.recv(1024).decode())

                    # Receive data from server and save it to an audio file
                    data = b''
                    received_size = 0
                    while received_size < file_size:
                        chunk = self.client_socket.recv(1024)
                        data += chunk
                        received_size += len(chunk)

                    
                    # Write the received data to a temporary audio file
                    project_directory = os.path.abspath(os.path.dirname(__file__))
                    current_directory = os.path.join(project_directory, "resource")               
                    temp_file_path = os.path.join(current_directory, "temp_audio.mp3")
                    with open(temp_file_path, 'wb') as temp_file:
                        temp_file.write(data)

                    # Play the received audio
                    self.play_audio(temp_file_path)

                    # Wait for 5 minutes (300 seconds)
                    time.sleep(300)
                # If the server sends a special command, you can break the loop and close the connection
                if response == 'CLOSE':
                    break

            except Exception as e:
                # If an error occurs (like the server disconnecting), print the error and break the loop
                print("Error:", str(e))
                break
    def receive(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                self.song_listbox.insert(self.window.END, message)
            except:
                print('An error occurred!')
                self.client_socket.close()
                break            
    # Function to play audio
    def play_audio(self,data):
        try:
            print("ĐANG GỌI HÀM PLAY AUDIO")
            mixer.music.load(data)
            mixer.music.set_volume(0.7) 
            mixer.music.play()
        except Exception as e:  
            print("An error occurred while trying to play the audio:", str(e))