
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import os
import subprocess
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
import threading
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUTPUT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_PATH = os.path.join(OUTPUT_PATH, "GUI\\assets\\frame1")
from BLL import UserBLL

def on_forgot_password_click(event):
    print("Forgot password clicked")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def create_rounded_rect(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)
class Login:
    def __init__(self):
        self.window = Tk()
        self.window.title("Login")
        self.window.geometry("400x650")
        self.window.configure(bg = "#FFFFFF")
        

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 650,
            width = 400,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            400.0,
            650.0,
            fill="#FFFFFF",
            outline="")
        #Background image
        self.background_image = ImageTk.PhotoImage(file=relative_to_assets("BackGround.png"))
        self.canvas.create_image(0,0,image=self.background_image,anchor=NW)

        #Logo image
        self.logo_image = PhotoImage(file=relative_to_assets("Hub.png"))
        self.logo_image_1 = self.canvas.create_image(
            200.0,
            110.0,
            image=self.logo_image
        )
        #Login Button
        self.login_button = Button(  
            borderwidth=0,
            highlightthickness=0,
            command=self.run_gui,
            relief="flat",
            background="#3B66FF",
            text="Login",
            font=("Inter Medium", 24 * -1),
            fg="#FFFFFF"
        )
        self.login_button.place(
            x=94.0,
            y=399.0,
            width=212.0,
            height=54.0
        )
        #Note image
        self.note_image = PhotoImage(file=relative_to_assets("Note.png"))
        self.note_image_1=self.canvas.create_image(
            360.0,
            30.0,
            image=self.note_image
            )
        
        self.user_field=create_rounded_rect(self.canvas, 
                                    61.0, 
                                    208.0, 
                                    352.0, 
                                    261.0, 
                                    radius=25, 
                                    fill="#F3F2F2", 
                                    outline="")
        self.password_field=create_rounded_rect(self.canvas,
                                                61.0,
                                                275.0,
                                                352.0,
                                                328.0,
                                                fill="#F3F2F2",
                                                outline="")
        
        self.user_input = Entry( width=18, bd=0, bg="#F3F2F2", font=("Inter Medium", 20 * -1), fg="#AAAAAA")
        self.user_input.place(x=110.0, y=230.0, height=15.0)
        self.user_input.bind("<FocusIn>", self.clear_hint)
        self.user_input.bind("<FocusOut>", self.restore_hint)
        self.user_input.bind("<Return>", lambda event: self.password_input.focus())
        self.user_input.insert(0, "Enter Username")
        
        #Show password icon
        self.show_password_image = PhotoImage(file=relative_to_assets("Closed Eye.png"))
        self.show_password_button=Button(
            image=self.show_password_image,
            relief="flat",
            highlightthickness=0,
            bd=0,
            command=lambda: self.toggle_password(),
            background="#F3F2F2",
            activebackground="#F3F2F2"
        )
        self.show_password_button.place(x=322.0, y=285.0)
        
        # Create a BooleanVar to track whether the password is shown or hidden
        self.password_shown = BooleanVar()
        self.password_shown.set(False)

        self.password_input = Entry( width=18, bd=0, bg="#F3F2F2", font=("Inter Medium", 20 * -1), fg="#AAAAAA",show="*")
        self.password_input.place(x=110.0, y=295.0, height=15.0)
        self.password_input.bind("<FocusIn>", self.clear_hint)
        self.password_input.bind("<FocusOut>", self.restore_hint)
        self.password_input.bind("<Return>", lambda event: self.login_button.invoke())
        self.password_input.insert(0, "Enter Password")
        
        #Password and User icon
        self.password_image = PhotoImage(file=relative_to_assets("Password.png"))
        self.password_image_1=self.canvas.create_image(
            85.0,
            300.0,
            image=self.password_image)

        self.user_image = PhotoImage(file=relative_to_assets("User.png"))
        self.user_image_1=self.canvas.create_image(
            85.0,
            235.0,
            image=self.user_image)
        
        # Forgot password text
        self.forgot_password_text=self.canvas.create_text(
            260.0,
            338.0,
            anchor="nw",
            text="Forgot password?",
            fill="#FFFFFF",
            font=("Inter ExtraBold", 12 * -1, "underline"),
            tags="forgot_password_text"
        )

        self.canvas.tag_bind("forgot_password_text", "<Button-1>", on_forgot_password_click)
        self.canvas.create_text(
            25.0,
            55.0,
            anchor="nw",
            text="Login",
            fill="#FFFFFF",
            font=("Inter Medium", 15 * -1)
        )

        #Facebook and Google icon
        self.facebook_image = PhotoImage(
            file=relative_to_assets("Facebook.png"))
        self.facebook_image_1=self.canvas.create_image(
            240.0,
            577.0,
            image=self.facebook_image)

        self.google_image = PhotoImage(
            file=relative_to_assets("Google.png"))
        self.google_image_image_1=self.canvas.create_image(
            170.0,
            577.0,
            image=self.google_image)

        self.canvas.create_text(
            150.0,
            521.0,
            anchor="nw",
            text="Or Sign In With",
            fill="#FFFFFF",
            font=("Inter Medium", 16 * -1)
        )
    def clear_hint(self,event):
        current = event.widget.get()
        if current == "Enter Username" or current == "Enter Password":
            event.widget.delete(0, END)
            event.widget.config(fg="#000000")  

    def restore_hint(self,event):
        current = event.widget.get()
        if current == "":
            if event.widget == self.user_input:
                event.widget.insert(0, "Enter Username")
            elif event.widget == self.password_input:
                event.widget.insert(0, "Enter Password")
            event.widget.config(fg="#AAAAAA")  
    def toggle_password(self):
        # If the password is currently shown, hide it
        if self.password_shown.get():
            self.password_input.config(show="*")
            self.password_shown.set(False)
        # If the password is currently hidden, show it
        else:
            self.password_input.config(show="")
            self.password_shown.set(True)
    def run(self):
        self.window.resizable(False, False)
        self.window.mainloop()
    def run_gui(self):
        username = self.user_input.get()
        password = self.password_input.get()
        if UserBLL.UserBLL.checkUsernameAndPass(self,username, password):
            subprocess.Popen(["python", "GUI/gui.py"])
            self.window.destroy()
        else:
            messagebox.showerror("Error", "Invalid username or password")
if __name__ == "__main__":
    login = Login()
    login.run()