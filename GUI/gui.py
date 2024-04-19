
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
import os
import sys
import threading
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from DAL.PlayListDAL import PlayListDAL
from SocketTest.client import ClientListener 
from tkinter import Tk  # Import the Tk class
from tkinter import Canvas, Entry, Text, Button, PhotoImage, Listbox, Scrollbar, Menubutton, Menu, filedialog
import socket
import json

OUTPUT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_PATH = os.path.join(OUTPUT_PATH, "GUI\\assets\\frame0")


        
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Presentation:  
    def __init__(self):
        self.window = Tk()
        self.window.title("HarmonyHub")
        self.window.geometry("700x500")
        self.window.configure(bg="#FFFFFF")
        self.play_list = PlayListDAL()
        #self.client = ClientListener()
       
        self.canvas = Canvas(
                self.window,
                bg = "#FFFFFF",
                height = 500,
                width = 700,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )
    
        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            208.0,
            437.0,
            fill="#2D2D2D",
            outline="")

        self.canvas.create_rectangle(
            208.0,
            0.0,
            700.0,
            437.0,
            fill="#787575",
            outline="")

        self.canvas.create_rectangle(
            0.0,
            437.0,
            700.0,
            500.0,
            fill="#FF9800",
            outline="")

        self.canvas.create_rectangle(
            208.0,
            408.0,
            700.0,
            437.0,
            fill="#313131",
            outline="")
        
        song_listbox = Listbox(self.window, bg="#D9D9D9", fg="#000000", font=("Inter ExtraBold", 10))
        
        song_listbox.place(
            x=208.0,
            y=47.0,
            width=170.0,
            height=350.0
        )
        song_listbox.insert(0, "Song 1")
        song_listbox.insert(1, "Song 2")
        Scrollbar_1 = Scrollbar(self.window, orient="vertical")
        Scrollbar_1.config(command=song_listbox.yview)
        song_listbox.config(yscrollcommand=Scrollbar_1.set)
        Scrollbar_1.place(
            x=378.0,
            y=47.0,
            width=20.0,
            height=350.0
        )
        
        self.button_image_4=PhotoImage(file=relative_to_assets("Circled Play.png"))
        
        self.button_4=Button(
            image=self.button_image_4,
            command=lambda: self.play_selected_track(),
            borderwidth=0,
            relief="sunken",
            bg="#FF9900",
            activebackground="#FF9900",
            height=30,
            width=46
            )
        self.button_4.place(
            x=72.0,
            y=446.0
        )
        
        self.image_image_1 = PhotoImage(file=relative_to_assets("Hub.png"))
        self.image_1=self.canvas.create_image(
            15.0,
            12.0,  
            image = self.image_image_1
            )
        self.button_image_6= PhotoImage(file=relative_to_assets("End.png"))
        self.button_6=Button(
            image=self.button_image_6,
            borderwidth=0,
            relief="sunken",
            bg="#FF9900",
            activebackground="#FF9900",
            height=35,
            width=46)
        self.button_6.place(
            x=178.0,
            y=443.0,
        )
        self.button_image_3= PhotoImage(file=relative_to_assets("Skip to Start.png"))
        self.button_3=Button(
            image=self.button_image_3,
            borderwidth=0,
            relief="sunken",
            bg="#FF9900",
            activebackground="#FF9900",
            height=35,
            width=46)
        self.button_3.place(
            x=22.0,
            y=443.0
        )
        
        self.button_image_2= PhotoImage(file=relative_to_assets("Shuffle.png"))
        self.button_2=Button(    
            image= self.button_image_2,
            borderwidth=0,
            relief="sunken",
            bg="#FF9900",
            activebackground="#FF9900",
            height=30,
            width=40)
        self.button_2.place(
            x=125.0,
            y=470.0
        )
        
        self.button_image_5=PhotoImage(file=relative_to_assets("Repeat.png"))
        
        self.button_5=Button(
            image= self.button_image_5,
            borderwidth=0,
            relief="sunken",
            bg="#FF9900",
            activebackground="#FF9900",
            height=15,
            width=40
            )
        self.button_5.place(
            x=75.0,
            y=477.0
        )
        
        self.button_image_7= PhotoImage(file=relative_to_assets("Audio.png"))
        self.button_7=Button(
            image= self.button_image_7,
            borderwidth=0,
            relief="sunken",
            bg="#FF9900",
            activebackground="#FF9900",
            height=30,
            width=40)
        self.button_7.place(
            x=235.0,
            y=470.0
        )
        self.button_image_8=PhotoImage(file=relative_to_assets("Adjust.png"))
        self.button_8=Button(
            image= self.button_image_8,
            borderwidth=0,
            relief="sunken",
            bg="#FF9900",
            activebackground="#FF9900",
            height=30,
            width=40
            )
        self.button_8.place(
            x=367.0,
            y=470.0,
        )
        self.button_image_9=PhotoImage(file=relative_to_assets("Menu.png"))
        self.button_9=Menubutton(
            image= self.button_image_9,
            borderwidth=0,
            relief="sunken",
            bg="#313131",
            activebackground="#FF9900",
            height=20,
            width=40
            )
        self.button_9.place(
            x=660.0,
            y=410.0,
        )
        self.button_9.menu=Menu(self.button_9,tearoff = False)
        self.button_9["menu"]=self.button_9.menu
        self.button_9.menu.add_command(label="Select Folder")
        
        
        self.button_image_1=PhotoImage(file=relative_to_assets("Pause Button.png"))

        self.button_1=Button(
            image=self.button_image_1,
            borderwidth=0,
            relief="sunken",
            bg="#FF9900",
            activebackground="#FF9900",
            height=35,
            width=46
        )
        self.button_1.place(
            x=123,
            y=442
        )
        self.canvas.create_text(
            25.0,
            5.0,
            anchor="nw",
            text="HarmonyHub",
            fill="#FFFFFF",
            font=("Inter ExtraBold", 12 * -1)
        )

        self.canvas.create_rectangle(
            19.0,
            46.0,
            190.0,
            219.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            208.0,
            0.0,
            700.0,
            46.0,
            fill="#3F3F3F",
            outline="")
        self.image_image_2=PhotoImage(file=relative_to_assets("Search.png"))
        self.image_2=self.canvas.create_image(
            219.0,
            420.0,
            image=self.image_image_2
            )
        
    def run(self):
        self.window.resizable(False, False)
        self.window.mainloop()
        # receive_thread = threading.Thread(target=self.client.receive)
        # receive_thread.start()
    
if __name__ == "__main__":
    app = Presentation()
    app.run()
   