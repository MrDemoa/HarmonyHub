
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import os
from tkinter import Frame, Label, Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, font, messagebox, simpledialog, ttk
import sys
import threading
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from BLL.ArtistBLL import ArtistBLL
from BLL.TrackBLL import TrackBLL
from BLL.UserBLL import UserBLL
from DTO.ArtistDTO import ArtistDTO
from DTO.TrackDTO import TrackDTO
from DTO.UserDTO import UserDTO
from DAL.AlbumDAL import AlbumDAL
from DAL.ConnectDB import ConnectSQL
from BLL.AlbumBLL import AlbumBLL
from DTO.AlbumDTO import AlbumDTO
OUTPUT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_PATH = os.path.join(OUTPUT_PATH, "GUI\\assets\\frame2")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Admin:
    def __init__(self):
        self.window = Tk()
        self.window.title("Admin Panel")
        self.window.geometry("1000x700")
        self.window.configure(bg = "#FFFFFF")
        self.album = AlbumDAL()
        self.con = ConnectSQL.connect_mysql()
        

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 700,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            237.0,
            700.0,
            fill="#292929",
            outline="")

        self.canvas.create_rectangle(
            237.0,
            0.0,
            1000.0,
            48.0,
            fill="#B4B4B4",
            outline="")

        self.logo_image = PhotoImage(file=relative_to_assets("Hub.png"))
        self.logo_image_resized = self.logo_image.subsample(3, 3)
        self.logo_image_1 = self.canvas.create_image(
            30.0,
            27.0,
            image=self.logo_image_resized)

        self.canvas.create_text(
            52.0,
            19.0,
            anchor="nw",
            text="HarmonyHub ",
            fill="#FFFFFF",
            font=("Inter ExtraBold", 16 * -1,"bold")
        )
        #Line
        self.canvas.create_rectangle(
            0.5,
            48.0,
            237.5,
            48.0,
            fill="#FFFFFF",
            outline="")

        self.admin_icon = PhotoImage(file=relative_to_assets("admin.png"))
        self.admin_icon_1=self.canvas.create_image(
            939.0,
            27.0,
            image=self.admin_icon
            )

        self.canvas.create_text(
            797.0,
            17.0,
            anchor="nw",
            text="Hello Admin",
            fill="#FFFFFF",
            font=("Inter ExtraBold", 20 * -1)
        )
        #Albums
        self.canvas.create_text(
            70.0,
            88.0,
            anchor="nw",
            text="Albums",
            fill="#FFFFFF",
            font=("Inter", 24 * -1,"bold"),
            tags="album_text"
        )
        self.canvas.tag_bind("album_text", "<Button-1>", lambda x: self.show_frame(AlbumFrame))
        #Users
        self.canvas.create_text(
            72.0,
            337.0,
            anchor="nw",
            text="Users",
            fill="#FFFFFF",
            font=("Inter", 24 * -1,"bold"),
            tag="user_text"
        )
        self.canvas.tag_bind("user_text", "<Button-1>", lambda x: self.show_frame(UserFrame))
        #Tracks
        self.canvas.create_text(
            70.0,
            171.0,
            anchor="nw",
            text="Tracks",
            fill="#FFFFFF",
            font=("Inter", 24 * -1,"bold"),
            tag="track_text"
        )
        self.canvas.tag_bind("track_text", "<Button-1>", lambda x: self.show_frame(TrackFrame))
        #Artists
        self.canvas.create_text(
            70.0,
            254.0,
            anchor="nw",
            text="Artists",
            fill="#FFFFFF",
            font=("Inter", 24 * -1,"bold"),
            tag="artist_text"
        )
        self.canvas.tag_bind("artist_text", "<Button-1>", lambda x: self.show_frame(ArtistFrame))
        #Shut Down button
        self.shut_down_icon = PhotoImage(file=relative_to_assets("Shutdown.png"))
        self.shut_down_button=Button(   
            image=self.shut_down_icon,
            relief="flat",
            borderwidth=0,
            background="#2A2A2A",
            activebackground="#2A2A2A",
            command=lambda: print("Shutdown clicked"),
            )
        self.shut_down_button.place(
            x=83.0,
            y=631.0,
            width=80.0,
            height=60.0,)

        #Live button
        self.live_icon = PhotoImage(file=relative_to_assets("Live.png"))
        self.live_icon_1=Button(
            image=self.live_icon,
            command=lambda: self.change_text(),
            relief="flat",
            borderwidth=0,
            background="#FFFFFF",
            activebackground="#FFFFFF",
            
            )
        self.live_icon_1.place(
            x=920.0,
            y=630.0,
            width=60,
            height=42
        )
        self.label_font = font.Font(family="Inter ExtraBold", size=18, weight="bold")
        self.label = Label(
            self.window,
            text="Server Offline",
            bg="#FFFFFF",
            fg="#000000",
            font=self.label_font
        )
        self.label.place(
            x=760.0,
            y=635.0,
        )
        # self.canvas.create_text(
        #     778.0,
        #     639.0,
        #     anchor="nw",
        #     text="Server Offline",
        #     fill="#000000",
        #     font=("Inter ExtraBold", 20 * -1,"bold")
        # )
        
        #Decorative 
        self.canvas.create_rectangle(
            40.0,
            453.9756164550781,
            204.0,
            454.999999998603,
            fill="#FFFFFF",
            outline="")
        self.medal_icon = PhotoImage(file=relative_to_assets("medal.png"))
        self.medal_icon_1=self.canvas.create_image(
            120.0,
            485.0,
            image=self.medal_icon
            )
        self.big_frame = Frame(self.window,background="#FFFFFF")
        self.big_frame.place(x=285.0, y=70.0, width=665.0, height=520.0)
        # Create the smaller frames and add them to the big frame
        self.frames = {}
        for F in (AlbumFrame, TrackFrame, ArtistFrame, UserFrame):
            frame = F(self.big_frame, self,self.con)
            frame.configure(background='#FFFFFF')
            self.frames[F] = frame
            frame.place(x=0, y=0, width=665.0, height=520.0,)

        # Show the first frame
        self.show_frame(AlbumFrame)
    def change_text(self):
        if self.label["text"] == "Server Offline":
            self.label["text"] = "Server Online"
            self.label["fg"] = "#00FF00"
        else:
            self.label["text"] = "Server Offline"
            self.label["fg"] = "#000000"
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
    def show_dialog_album(self):
        dialog = Toplevel(self.window)
        dialog.title("Input")

        labels = ["ALbum ID", "Title", "Artist ID", "Genre", "Release Date"]
        entries = []

        for i, label in enumerate(labels):
            Label(dialog, text=label).grid(row=i, column=0)
            entry = Entry(dialog)
            entry.grid(row=i, column=1)
            entries.append(entry)

        Button(dialog, text="Submit", command=lambda: self.process_entries_album(entries)).grid(row=len(labels), column=0, columnspan=2)

    def process_entries_album(self, entries,dialog):
        try:
            album_dto = AlbumDTO(
                albumID=entries[0].get(),
                title=entries[1].get(),
                artistID=entries[2].get(),
                genre=entries[3].get(),
                releasedate=entries[4].get()
            )
            AlbumBLL.insert(album_dto)
            messagebox.showinfo("Success", "Album inserted successfully")
            dialog.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def show_dialog_track(self):
        dialog = Toplevel(self.window)
        dialog.title("Input")

        labels = ["Track ID", "Title", "Album ID", "Genre", "Duration","Release Date"]
        entries = []

        for i, label in enumerate(labels):
            Label(dialog, text=label).grid(row=i, column=0)
            entry = Entry(dialog)
            entry.grid(row=i, column=1)
            entries.append(entry)

        Button(dialog, text="Submit", command=lambda: self.process_entries_track(entries)).grid(row=len(labels), column=0, columnspan=2)
    def process_entries_track(self, entries,dialog):
        try:
            track_dto = TrackDTO(
                trackID=entries[0].get(),
                title=entries[1].get(),
                albumID=entries[2].get(),
                genre=entries[3].get(),
                duration=entries[4].get(),
                releasedate=entries[5].get()
            )
            TrackBLL.insert(track_dto)
            messagebox.showinfo("Success", "Track inserted successfully")
            dialog.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def show_dialog_artist(self):
        dialog = Toplevel(self.window)
        dialog.title("Input")

        labels = ["Artist ID", "Name", "Genre"]
        entries = []

        for i, label in enumerate(labels):
            Label(dialog, text=label).grid(row=i, column=0)
            entry = Entry(dialog)
            entry.grid(row=i, column=1)
            entries.append(entry)

        Button(dialog, text="Submit", command=lambda: self.process_entries_artist(entries)).grid(row=len(labels), column=0, columnspan=2)
    def process_entries_artist(self, entries,dialog):
        try:
            artist_dto = ArtistDTO(
                artistID=entries[0].get(),
                name=entries[1].get(),
                genre=entries[2].get()
            )
            ArtistBLL.insert(artist_dto)
            messagebox.showinfo("Success", "Artist inserted successfully")
            dialog.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def show_dialog_user(self):
        dialog = Toplevel(self.window)
        dialog.title("Input")

        labels = ["User ID", "Username", "Email", "Role"]
        entries = []

        for i, label in enumerate(labels):
            Label(dialog, text=label).grid(row=i, column=0)
            entry = Entry(dialog)
            entry.grid(row=i, column=1)
            entries.append(entry)

        Button(dialog, text="Submit", command=lambda: self.process_entries_user(entries)).grid(row=len(labels), column=0, columnspan=2)
    def process_entries_user(self, entries,dialog):
        try:
            user_dto = UserDTO(
                userID=entries[0].get(),
                username=entries[1].get(),
                email=entries[2].get(),
                role=entries[3].get()
            )
            UserBLL.insert(user_dto)
            messagebox.showinfo("Success", "User inserted successfully")
            dialog.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def run(self):
        self.window.resizable(False, False)
        self.window.mainloop()

class AlbumFrame(Frame):
    def __init__(self, parent, big_frame,con):
        super().__init__(parent)
        self.pack(fill='both', expand=True)
        self.con = con
        #Add Album button
        self.add_album_button = Button(
            self,
            background="#4394AE",
            text="Add Albums",
            font=("Inter Medium", 20 * -1,"bold"),
            fg="#FFFFFF",
            relief="flat",
            activebackground="#4394AE",
            activeforeground="#FFFFFF",
            command=lambda: big_frame.show_dialog_album()
        )

        self.add_album_button.place(
            x=480.0,
            y=0.0,
            width=174.0,
            height=43.0,
            )
        
        #Table
        self.album_table = ttk.Treeview(self, columns=("Album ID","Title", "Artist ID", "Genre", "Release Date","Action"), show='headings')
        self.album_table.heading("Album ID", text="Album ID")
        self.album_table.heading("Title", text="Title")
        self.album_table.heading("Artist ID", text="Artist ID")
        self.album_table.heading("Genre", text="Genre")
        self.album_table.heading("Release Date", text="Release Date")
        self.album_table.heading("Action", text="Action")

        self.album_table.column("Album ID", width=100, anchor='center')
        self.album_table.column("Title", width=100, anchor='center')
        self.album_table.column("Artist ID", width=100, anchor='center')
        self.album_table.column("Genre", width=100, anchor='center')
        self.album_table.column("Release Date", width=100, anchor='center')
        self.album_table.column("Action", width=100, anchor='center')

        self.album_table.place(
            x=0,
            y=70,
            width=665.0,
            height=480.0
            )
        self.insert_into_table_album() 
    def insert_into_table_album(self):
        # Create a cursor
        cursor = self.con.cursor()

        # Execute a query to fetch all rows from the album table
        cursor.execute("SELECT * FROM album")

        # Fetch all rows
        rows = cursor.fetchall()

        # Insert each row into the table
        for row in rows:
            self.album_table.insert('', 'end', values=row)

        # Close the cursor
        cursor.close() 
      
class TrackFrame(Frame):
    def __init__(self, parent, big_frame,con):
        super().__init__(parent)
        self.pack(fill='both', expand=True)
        self.con = con
        #Add Tracks button
        self.add_track_button = Button(
            self,
            background="#4394AE",
            text="Add Tracks",
            font=("Inter Medium", 20 * -1,"bold"),
            fg="#FFFFFF",
            relief="flat",
            activebackground="#4394AE",
            activeforeground="#FFFFFF",
            command=lambda: big_frame.show_dialog_track()
        )

        self.add_track_button.place(
            x=480,
            y=0,
            width=174.0,
            height=43.0,
            )
        #Table

        self.track_table = ttk.Treeview(self, columns=("Track ID","Title", "Album ID", "Genre", "Duration","Release Date","Action"), show='headings')
        self.track_table.heading("Track ID", text="Track ID")
        self.track_table.heading("Title", text="Title")
        self.track_table.heading("Album ID", text="Album ID")
        self.track_table.heading("Genre", text="Genre")
        self.track_table.heading("Duration", text="Duration")
        self.track_table.heading("Release Date", text="Release Date")
        self.track_table.heading("Action", text="Action")

        self.track_table.column("Track ID", width=75, anchor='center')
        self.track_table.column("Title", width=100, anchor='center')
        self.track_table.column("Album ID", width=100, anchor='center')
        self.track_table.column("Genre", width=100, anchor='center')
        self.track_table.column("Duration", width=100, anchor='center')
        self.track_table.column("Release Date", width=100, anchor='center')
        self.track_table.column("Action", width=90, anchor='center')
     
        self.track_table.place(
            x=0,
            y=70,
            width=665.0,
            height=480.0
            )
        self.insert_into_table_track()
    def insert_into_table_track(self):
            # Create a cursor
            cursor = self.con.cursor()

            # Execute a query to fetch all rows from the album table
            cursor.execute("SELECT * FROM track")

            # Fetch all rows
            rows = cursor.fetchall()

            # Insert each row into the table
            for row in rows:
                self.track_table.insert('', 'end', values=row)

            # Close the cursor
            cursor.close()
class ArtistFrame(Frame):
    def __init__(self, parent, big_frame,con):
        super().__init__(parent)
        self.pack(fill='both', expand=True)
        self.con = con
        self.add_artist_button = Button(
            self,
            background="#4394AE",
            text="Add Artists",
            font=("Inter Medium", 20 * -1,"bold"),
            fg="#FFFFFF",
            relief="flat",
            activebackground="#4394AE",
            activeforeground="#FFFFFF",
            command=lambda: big_frame.show_dialog_artist()
        )
        self.add_artist_button.place(
            x=480.0,
            y=0.0,
            width=174.0,
            height=43.0,
            )
        #Table
        self.artist_table = ttk.Treeview(self, columns=("Artist ID","Name", "Genre","Action"), show='headings')
        self.artist_table.heading("Artist ID", text="Artist ID")
        self.artist_table.heading("Name", text="Name")
        self.artist_table.heading("Genre", text="Genre")
        self.artist_table.heading("Action", text="Action")

        self.artist_table.column("Artist ID", width=100, anchor='center')
        self.artist_table.column("Name", width=100, anchor='center')
        self.artist_table.column("Genre", width=100, anchor='center')
        self.artist_table.column("Action", width=100, anchor='center')

        self.artist_table.place(
            x=0,
            y=70,
            width=665.0,
            height=480.0
            )
        self.insert_into_table_artist()
    def insert_into_table_artist(self):
        # Create a cursor
        cursor = self.con.cursor()

        # Execute a query to fetch all rows from the album table
        cursor.execute("SELECT * FROM artist")

        # Fetch all rows
        rows = cursor.fetchall()

        # Insert each row into the table
        for row in rows:
            self.artist_table.insert('', 'end', values=row)

        # Close the cursor
        cursor.close()
class UserFrame(Frame):
    def __init__(self, parent, big_frame,con):
        super().__init__(parent)
        self.pack(fill='both', expand=True)
        self.con = con
        self.add_user_button = Button(
            self,
            background="#4394AE",
            text="Add Users",
            font=("Inter Medium", 20 * -1,"bold"),
            fg="#FFFFFF",
            relief="flat",
            activebackground="#4394AE",
            activeforeground="#FFFFFF",
            command=lambda: big_frame.show_dialog_user()
        )
        self.add_user_button.place(
            x=480.0,
            y=0.0,
            width=174.0,
            height=43.0,
            )
        #Table     
        self.user_table = ttk.Treeview(self, columns=("User ID","Username", "Email", "Role","Action"), show='headings')
        self.user_table.heading("User ID", text="User ID")
        self.user_table.heading("Username", text="Username")
        self.user_table.heading("Email", text="Email")
        self.user_table.heading("Role", text="Role")
        self.user_table.heading("Action", text="Action")
        
        self.user_table.column("User ID", width=100, anchor='center')
        self.user_table.column("Username", width=100, anchor='center')
        self.user_table.column("Email", width=100, anchor='center')
        self.user_table.column("Role", width=100, anchor='center')
        self.user_table.column("Action", width=100, anchor='center')
        
        self.user_table.place(
            x=0,
            y=70,
            width=665.0,
            height=480.0
            )
        self.insert_into_table_user()
    def insert_into_table_user(self):
        # Create a cursor
        cursor = self.con.cursor()

        # Execute a query to fetch all rows from the album table
        cursor.execute("SELECT * FROM user")

        # Fetch all rows
        rows = cursor.fetchall()

        # Insert each row into the table
        for row in rows:
            self.user_table.insert('', 'end', values=row)

        # Close the cursor
        cursor.close()
if __name__ == "__main__":
    admin = Admin()
    admin.run()