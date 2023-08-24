import customtkinter as ctk
import tkinter as tk
import cv2
from tkinter import messagebox
from PIL import Image, ImageTk

# Create a Bootstrap-inspired color palette
bootstrap_bg = "#1E1E1E"
bootstrap_fg = "#FFFFFF"
bootstrap_button = "#007BFF"
bootstrap_button_hover = "#0056b3"
drone_box = "#fff"

# Font size and style
label_font = ("Helvetica", 24)
button_font = ("Helvetica", 14, "bold")
entry_font = ("Helvetica", 16)




# Login page
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Login")
        self.geometry("400x600")

        # Login page logo
        self.image = Image.open("logo.png")
        self.image = self.image.resize((200, 200)) 
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = ctk.CTkLabel(self, image=self.photo, text="")
        self.image_label.pack(pady=5)

        # Username labels / entrys
        self.usernameLabel = ctk.CTkLabel(self, font=label_font, text="Name")
        self.usernameLabel.pack(pady=5)

        self.usernameEntry = ctk.CTkEntry(self, font=entry_font, placeholder_text="Username", justify=tk.CENTER)
        self.usernameEntry.pack(pady=5)

        # Password labels / entrys
        self.passwordLabel = ctk.CTkLabel(self, font=label_font, text="Password")
        self.passwordLabel.pack(pady=5)

        self.passwordEntry = ctk.CTkEntry(self, font=entry_font, placeholder_text="Password", justify=tk.CENTER)
        self.passwordEntry.pack(pady=5)

        # login Button
        self.loginButton = ctk.CTkButton(self, font=button_font, text="Login", command=self.login)
        self.loginButton.pack(pady=10)







    def login(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()

        users = {
            "admin": "admin",
            # Add more users here
        }

        if username in users and users[username] == password:
            messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
            self.destroy()
            new_app = mainpage()
            new_app.mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")




# Create the new window
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

class mainpage(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Main page")
        self.geometry("600x300")

        self.columnconfigure(0, weight=1)  # Make column 0 expandable
        self.rowconfigure(1, weight=1)     # Make row 1 expandable
        self.rowconfigure(2, weight=1)     # Make row 2 expandable

        # Create widgets for the new window
        page2_label = ctk.CTkLabel(self, text="Welcome to Fireguard homepanel")
        page2_label.grid(row=1, column=0, pady=10, sticky="nsew")


        # Drone 1
        image = Image.open("logo.png")
        new_size = (75, 75)
        resized_image = image.resize(new_size, Image.LANCZOS)

        photo = ImageTk.PhotoImage(resized_image)

        label = ctk.CTkLabel(self, image=photo)
        label.image = photo
        label.grid(row=2, column=1, pady=10, sticky="ns")


        # Drone 2
        image = Image.open("logo.png")
        new_size = (75, 75)
        resized_image = image.resize(new_size, Image.LANCZOS)

        photo = ImageTk.PhotoImage(resized_image)

        label = ctk.CTkLabel(self, image=photo)
        label.image = photo
        label.grid(row=2, column=2, pady=10, sticky="ns")


        # Drone 3
        image = Image.open("logo.png")
        new_size = (75, 75)
        resized_image = image.resize(new_size, Image.LANCZOS)

        photo = ImageTk.PhotoImage(resized_image)

        label = ctk.CTkLabel(self, image=photo)
        label.image = photo
        label.grid(row=2, column=3, pady=10, sticky="ns")


        # Drone 4
        image = Image.open("logo.png")
        new_size = (75, 75)
        resized_image = image.resize(new_size, Image.LANCZOS)

        photo = ImageTk.PhotoImage(resized_image)

        label = ctk.CTkLabel(self, image=photo)
        label.image = photo
        label.grid(row=2, column=4, pady=10, sticky="ns")



        close_button = ctk.CTkButton(self, text="Logout", command=self.destroy)
        close_button.grid(row=3, column=0, pady=10, sticky="ns")


if __name__ == "__main__":
    appWidth, appHeight = 600, 700
    app = App()
    app.mainloop()