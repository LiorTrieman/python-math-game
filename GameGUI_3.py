# starting from the begining with Sentdex

from tkinter import *
from PIL import Image,ImageTk


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Math Game By Lior Trieman")
        self.pack(fill=BOTH, expand=1)
        quit_button = Button(self, text="Quit", command=self.client_exit)
        quit_button.place(x=1, y=1)


    def client_exit(self):
        exit()

# making a basic window:


root = Tk()
root.geometry("700x500")
app = Window(root)
root.mainloop()
