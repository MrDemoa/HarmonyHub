
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
from SocketTest.client import ClientListener
from GUI.Login import Login

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
class Signup:
    def __init__(self):
        self.window = Tk()
        self.window.title("Sign up")
        self.window.geometry("400x650")
        self.window.configure(bg = "#FFFFFF")
        self.host_ip = '127.0.0.1'
        self.port = 6767
        
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
        #Sign up Button
        self.sign_up_button = Button(  
            borderwidth=0,
            highlightthickness=0,
            command=self.finish_sign_up,
            relief="flat",
            background="#3B66FF",
            text="Sign up",
            font=("Inter Medium", 24 * -1),
            fg="#FFFFFF"
        )
        self.sign_up_button.place(
            x=94.0,
            y=500.0,
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
        self.re_password_field=create_rounded_rect(self.canvas,
                                                61.0,
                                                342.0,
                                                352.0,
                                                395.0,
                                                fill="#F3F2F2",
                                                outline="")
        self.email_field=create_rounded_rect(self.canvas,
                                                61.0,
                                                409.0,
                                                352.0,
                                                462.0,
                                                fill="#F3F2F2",
                                                outline="")
        
        self.user_input = Entry( width=18, bd=0, bg="#F3F2F2", font=("Inter Medium", 20 * -1), fg="#AAAAAA")
        self.user_input.place(x=110.0, y=225.0, height=25.0)
        self.user_input.bind("<FocusIn>", self.clear_hint)
        self.user_input.bind("<FocusOut>", self.restore_hint)
        self.user_input.bind("<Return>", lambda event: self.password_input.focus_set())
        self.user_input.insert(0, "Enter Username")
        
        
        # Create a BooleanVar to track whether the password is shown or hidden
        self.password_shown = BooleanVar()
        self.password_shown.set(False)

        self.password_input = Entry( width=18, bd=0, bg="#F3F2F2", font=("Inter Medium", 20 * -1), fg="#AAAAAA")
        self.password_input.place(x=110.0, y=290.0, height=25.0)
        self.password_input.bind("<FocusIn>", self.clear_hint)
        self.password_input.bind("<FocusOut>", self.restore_hint)
        self.password_input.bind("<Return>", lambda event: self.re_enter_password_input.focus_set())
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
        self.email_image = PhotoImage(file=relative_to_assets("Email.png"))
        self.email_image_1=self.canvas.create_image(
            85.0,
            437.0,
            image=self.email_image)
        
        #Enter password
        self.password_shown = BooleanVar()
        self.password_shown.set(False)
        
        self.re_enter_password_input = Entry( width=18, bd=0, bg="#F3F2F2", font=("Inter Medium", 20 * -1), fg="#AAAAAA")
        self.re_enter_password_input.place(x=110.0, y=357.0, height=25.0)
        self.re_enter_password_input.bind("<FocusIn>", self.clear_hint)
        self.re_enter_password_input.bind("<FocusOut>", self.restore_hint)
        self.re_enter_password_input.bind("<Return>", lambda event: self.email_input.focus_set())
        self.re_enter_password_input.insert(0, "Confirm Password")
        
        #Re enter Password 
        self.password_image_2=self.canvas.create_image(
            85.0,
            365.0,
            image=self.password_image)
        #Email
        self.email_input = Entry( width=18, bd=0, bg="#F3F2F2", font=("Inter Medium", 20 * -1), fg="#AAAAAA")
        self.email_input.place(x=110.0, y=424.0, height=25.0)
        self.email_input.bind("<FocusIn>", self.clear_hint)
        self.email_input.bind("<FocusOut>", self.restore_hint)
        self.email_input.bind("<Return>", lambda event: self.sign_up_button.invoke())
        self.email_input.insert(0, "Enter Email")
        
        
        # Forgot password text
        self.login_text=self.canvas.create_text(
            270.0,
            580.0,
            anchor="nw",
            text="Login now",
            fill="#FFFFFF",
            font=("Inter ExtraBold", 16 * -1, "underline"),
            tags="login_text"
        )

        self.canvas.tag_bind("login_text", "<Button-1>", lambda x: self.run_login())
        self.canvas.create_text(
            25.0,
            55.0,
            anchor="nw",
            text="Sign up",
            fill="#FFFFFF",
            font=("Inter Medium", 15 * -1)
        )

        self.canvas.create_text(
            80.0,
            580.0,
            anchor="nw",
            text="Already have an account?",
            fill="#FFFFFF",
            font=("Inter Medium", 16 * -1)
        )
        
    def show_dialog_resetpassword(self):
        dialog = Toplevel(self.window,background="#272E41")
        dialog.title("Reset Password")
        dialog.grid_rowconfigure(0, weight=1)
        
        entries = []
        Label(dialog, text="Username", font=("Inter Medium", 20 * -1),background="#272E41",fg="#FFFFFF").grid(row=0, column=0)
        entries.append(Entry(dialog, width=18, bd=0, bg="#F3F2F2", font=("Inter Medium", 20 * -1)))
        entries[0].grid(row=0, column=1)
        Label(dialog, text="New Password", font=("Inter Medium", 20 * -1),background="#272E41",fg="#FFFFFF").grid(row=1, column=0)
        entries.append(Entry(dialog, width=18, bd=0, bg="#F3F2F2", font=("Inter Medium", 20 * -1)))
        entries[1].grid(row=1, column=1)
        
            
        Button(dialog, text="Reset Password", command=lambda: self.process_entry_resetpassword(entries,dialog)).grid(row=2, column=0, columnspan=2)
            
    def process_entry_resetpassword(self,entries,dialog):
        try:
            username = entries[0].get()
            new_password = entries[1].get()
            ClientListener.resetPassword(self, username, new_password)
                
            messagebox.showinfo("Success", "Password reset successfully")
            dialog.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
                
    def clear_hint(self,event):
        current = event.widget.get()
        if current == "Enter Username" or current == "Enter Password" or current == "Confirm Password" or current == "Enter Email":
            event.widget.delete(0, END)
            event.widget.config(fg="#000000")  

    def restore_hint(self,event):
        current = event.widget.get()
        if current == "":
            if event.widget == self.user_input:
                event.widget.insert(0, "Enter Username")
            elif event.widget == self.password_input:
                event.widget.insert(0, "Enter Password")
            elif event.widget == self.re_enter_password_input:
                event.widget.insert(0, "Confirm Password")
            elif event.widget == self.email_input:
                event.widget.insert(0, "Enter Email")
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
    def finish_sign_up(self):
        username = self.user_input.get()
        password = self.password_input.get() 
        if ClientListener.checkLogin(self, username, password):
            subprocess.Popen(["python", "GUI/Login.py"])
            self.window.destroy()
        else:
            messagebox.showerror("Error", "Invalid username or password")
    def run_login(self):
        self.window.destroy()
        login = Login()
        login.run()
if __name__ == "__main__":
    signup = Signup()
    signup.run()
    client = ClientListener()