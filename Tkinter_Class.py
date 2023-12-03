from tkinter import *
from tkinter import ttk


class TkinterGUI():
    """ This is a Tkinter class (Good for Labels, Buttons, CheckButton, EntryInput). """
    def __init__(self):
        """ Initialization for Tkinter. """
        global root, frm
        root = Tk()
        root.geometry('800x600+1300+1000')
        frm = ttk.Frame(root, padding=10)
        frm.grid()

    def Label(self, text, width, xcord, yxord, bg="white", fg="black", font="TkDefaultFont"):
        """ Label for Tkinter. """
        self.text = text
        self.width = width
        self.xcord = xcord
        self.yxord = yxord
        self.bg = bg
        self.fg = fg
        self.font = font
        ttk.Label(root, text=text, width=width, background=bg, foreground=fg, font=font).place(x=xcord, y=yxord)

    def Button(self, text, command, width, xcord, yxord):
        """ Button for Tkinter. """
        self.text = text
        self.command = command
        self.width = width
        self.xcord = xcord
        self.yxord = yxord
        ttk.Button(root, text=text, command=command, width=width).place(x=xcord, y=yxord)