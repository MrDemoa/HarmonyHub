# fileclient.py
from zeroconf import ServiceBrowser, Zeroconf
import socket 
import os
import time
from pygame import mixer
from zeroconf import ZeroconfServiceTypes
import threading

#
mixer.init()
# Class to handle user input in a separate thread
# class InputThread(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#         self.filename = None

#     def run(self):
#         self.filename = input("Enter the filename: ")

#     def get_filename(self):
#         return self.filename
# class MyListener:
#     # Function to play audio
#     def play_audio(self,data):
#         print("ĐANG GỌI HÀM PLAY AUDIO")
#         mixer.music.load(data)
#         mixer.music.set_volume(0.7) 
#         mixer.music.play()
        
#     def remove_service(self, zeroconf, type, name):
#         print("Service %s removed" % (name,))

#     def add_service(self, zeroconf, type, name):
#         info = zeroconf.get_service_info(type, name)
#         print("Service %s added, service info: %s" % (name, info))
#         if info:
#             SERVER_IP = socket.inet_ntoa(info.addresses[0])
#             SERVER_PORT = info.port
#             print("Server IP: ", SERVER_IP)
#             print("Server Port: ", SERVER_PORT)
            
#             # Connect to the server
#             client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             client.connect((SERVER_IP, SERVER_PORT))
#             # Initialize the InputThread instance
#             input_thread = InputThread()
#             input_thread.start()
#             # Wait for the InputThread to finish
#             input_thread.join()
#             # Get the filename from the user
#             filename = input_thread.get_filename()
            

#             if filename:
#                 client.send(filename.encode())
#                 # Rest of your code

#                 # Nhận dữ liệu từ server và lưu vào file audio
#                 data = b''
#                 while True:
#                     chunk = client.recv(1024)
#                     if not chunk:
#                         break
#                     data += chunk

#                 client.close()

#                 # Write the received data to a temporary audio file
#                 project_directory = os.path.abspath(os.path.dirname(__file__))
#                 current_directory = os.path.join(project_directory, "resource")               
#                 temp_file_path = os.path.join(current_directory, "temp_audio.mp3")
#                 with open(temp_file_path, 'wb') as temp_file:
#                     temp_file.write(data)

#                 # Play the received audio
#                 self.play_audio(temp_file_path)

#                 # Wait for 5 minutes (300 seconds)
#                 time.sleep(300)
                
#     def update_service(self, zeroconf, type, name):
#         print("Service %s updated" % (name,))


      
# zeroconf = Zeroconf()
# listener = MyListener()
# browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener)

# try:
#     while True:
#         time.sleep(1)
# except KeyboardInterrupt:
#     pass
# finally:
#     zeroconf.close()

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.bind(("", 6767))

# Listen for broadcast messages
data, addr = client_socket.recvfrom(1024)

# Extract server's IP address and port from the broadcast message
server_ip, server_port = data.decode().split(':')
client_socket.connect((server_ip, int(server_port)))