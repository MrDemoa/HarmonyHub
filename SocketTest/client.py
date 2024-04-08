# fileclient.py
from zeroconf import ServiceBrowser, Zeroconf
import socket 
import os
import time
from pygame import mixer
from pydub import AudioSegment
#
mixer.init()

class MyListener:
    # Function to play audio
    def play_audio(self,data):
        print("ĐANG GỌI HÀM PLAY AUDIO")
        mixer.music.load(data)
        mixer.music.set_volume(0.7) 
        mixer.music.play()
        
    def remove_service(self, zeroconf, type, name):
        print("Service %s removed" % (name,))

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        print("Service %s added, service info: %s" % (name, info))
        if info:
            SERVER_IP = socket.inet_ntoa(info.addresses[0])
            SERVER_PORT = info.port
            print("Server IP: ", SERVER_IP)
            print("Server Port: ", SERVER_PORT)
            
            # Connect to the server
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((SERVER_IP, SERVER_PORT))

            # Input filename from the user
            filename = input("Enter the filename: ")
            client.send(filename.encode())

            # Nhận dữ liệu từ server và lưu vào file audio
            data = b''
            while True:
                chunk = client.recv(1024)
                if not chunk:
                    break
                data += chunk

            client.close()

            # Write the received data to a temporary audio file
            project_directory = "C:\\Users\\ACER\\Desktop\\File C\\HarmonyHub\\SocketTest\\resource\\"
            temp_file_path = os.path.join(project_directory, "temp_audio.mp3")
            with open(temp_file_path, 'wb') as temp_file:
                temp_file.write(data)

            # Play the received audio
            self.play_audio(temp_file_path)

            # Wait for 5 minutes (300 seconds)
            time.sleep(300)
    def update_service(self, zeroconf, type, name):
        print("Service %s updated" % (name,))
zeroconf = Zeroconf()
listener = MyListener()
browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener)