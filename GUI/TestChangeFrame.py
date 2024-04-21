import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        # Create a container to hold all frames
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        # Dictionary to hold different frames
        self.frames = {}
        
        # Create and add frames to the dictionary
        for F in (AlbumFrame, TrackFrame, ArtistFrame, UsersFrame):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        # Show the first frame initially
        self.show_frame(AlbumFrame)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class AlbumFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Album Frame", font=("Helvetica", 18))
        label.pack(pady=10, padx=10)
        
        # Button to switch to the Track frame
        track_btn = tk.Button(self, text="Go to Track", command=lambda: controller.show_frame(TrackFrame))
        track_btn.pack(pady=5)
        
        # Button to switch to the Artist frame
        artist_btn = tk.Button(self, text="Go to Artist", command=lambda: controller.show_frame(ArtistFrame))
        artist_btn.pack(pady=5)
        
        # Button to switch to the Users frame
        users_btn = tk.Button(self, text="Go to Users", command=lambda: controller.show_frame(UsersFrame))
        users_btn.pack(pady=5)

class TrackFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Track Frame", font=("Helvetica", 18))
        label.pack(pady=10, padx=10)
        
        # Button to switch to the Album frame
        album_btn = tk.Button(self, text="Go to Album", command=lambda: controller.show_frame(AlbumFrame))
        album_btn.pack(pady=5)
        
        # Button to switch to the Artist frame
        artist_btn = tk.Button(self, text="Go to Artist", command=lambda: controller.show_frame(ArtistFrame))
        artist_btn.pack(pady=5)
        
        # Button to switch to the Users frame
        users_btn = tk.Button(self, text="Go to Users", command=lambda: controller.show_frame(UsersFrame))
        users_btn.pack(pady=5)
        label = tk.Label(self, text="Track Frame", font=("Helvetica", 18))
        label.pack(pady=10, padx=10)
class ArtistFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Artist Frame", font=("Helvetica", 18))
        label.pack(pady=10, padx=10)
        
        # Button to switch to the Album frame
        album_btn = tk.Button(self, text="Go to Album", command=lambda: controller.show_frame(AlbumFrame))
        album_btn.pack(pady=5)
        
        # Button to switch to the Track frame
        track_btn = tk.Button(self, text="Go to Track", command=lambda: controller.show_frame(TrackFrame))
        track_btn.pack(pady=5)
        
        # Button to switch to the Users frame
        users_btn = tk.Button(self, text="Go to Users", command=lambda: controller.show_frame(UsersFrame))
        users_btn.pack(pady=5)

class UsersFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Users Frame", font=("Helvetica", 18))
        label.pack(pady=10, padx=10)
        
        # Button to switch to the Album frame
        album_btn = tk.Button(self, text="Go to Album", command=lambda: controller.show_frame(AlbumFrame))
        album_btn.pack(pady=5)
        
        # Button to switch to the Track frame
        track_btn = tk.Button(self, text="Go to Track", command=lambda: controller.show_frame(TrackFrame))
        track_btn.pack(pady=5)
        
        # Button to switch to the Artist frame
        artist_btn = tk.Button(self, text="Go to Artist", command=lambda: controller.show_frame(ArtistFrame))
        artist_btn.pack(pady=5)

app = SampleApp()
app.geometry("400x300")
app.mainloop()
