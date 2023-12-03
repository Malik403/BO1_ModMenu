import pymem
from tkinter import messagebox
import gui_menu

#Connecting to game
try:
    game = pymem.Pymem("BlackOps.exe")
except pymem.exception.ProcessNotFound:
    messagebox.showerror('Connection Error', 'Error: Please Start the Game xD')
    message = messagebox.askquestion("Connection Error", "Is the game running?")
    if message == "yes":
        messagebox.showinfo("How-To", "Open Task Manager (CTRL + SHIFT + ESC)")
        messagebox.showinfo("", "Look for the BO1 game and write the name inside of the pymem variable!")
        messagebox.showinfo("", "Make sure you add the .exe extension!")
        messagebox.showinfo("", "Look in the Video folder inside of the program if you need more help!")
        exit()
    elif message == "no":
        messagebox.showinfo("Okay", "Please open the game and rerun the program")
        exit()
