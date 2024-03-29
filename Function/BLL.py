from tkinter import filedialog
import pygame
import os

# Business Logic Layer
class BusinessLogic:
    @staticmethod
    def load_music(data_access, listbox):
        folder_path = filedialog.askdirectory()
        if folder_path:
            for file in data_access.get_music_files(folder_path):
                listbox.insert('end', file)
        else:
            print("No folder selected.")
    @staticmethod
    def ping():
        print("Pong")