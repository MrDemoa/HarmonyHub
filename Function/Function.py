import pygame
import os

from tkinter import filedialog

import gui

def test() :
    print ("hello world")

def load_music():
        folder_path = filedialog.askdirectory()
        if folder_path:
            for file in os.listdir(folder_path):
                if file.endswith(".mp3"):  # or any other music file format
                    gui.Listbox_1.insert('end', file)
        else:
            print("No folder selected.")
def play_music():
    pygame.mixer.music.unpause()
    