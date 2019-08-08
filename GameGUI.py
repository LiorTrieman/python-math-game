# Game GUI with tkinter
# using code from stackoverflow: https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# welcome the useer to the game
# get user details and save them in a file

import tkinter as tk                # python 3
from tkinter import font as tkfont # python 3

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
# totaltxt.grid(row=0, sticky=E)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, Question_Screen):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Question_Screen(tk.Frame):  # the screen with the questions

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Please enter your answer and then press 'ENTER'", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        EnterButton = tk.Button(self, text="ENTER", bg="green",
                            command = lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="END GAME", bg="red",
                            command=lambda: controller.show_frame("PageTwo"))
        EnterButton.pack()
        button2.pack()



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Hi There! Would you like to play?", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Yes Please",bg="green",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="No Thank you", bg="red",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Good answer! please enter your details: ", font=controller.title_font, fg="dark blue")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back to home page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        buttonUserData = tk.Button(self, text="Save Your Info",
                           command=save_user_info_to_file)
        buttonUserData.pack()
        buttonStartGame = tk.Button(self, text="Lets Start Playing!",
                           command=lambda: controller.show_frame("Question_Screen"))
        buttonStartGame.pack()

        # user details entry screen

        label_1 = tk.Label(self, text="Name")
        label_2 = tk.Label(self, text="Password")
        entry_1 = tk.Entry(self)
        entry_2 = tk.Entry(self)
        label_1.pack()
        label_2.pack()
        entry_1.pack()
        entry_2.pack()

    def retrieve_input(self): # store input to variable
        inputValue = textBox.get("1.0", "end")
        print(inpurValue)

        textBox = Text(root)
        textBox.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Too Bad, See you next time!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="If you have second thoughts press here..:)", bg="orange",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

def save_user_info_to_file():
    pass


if __name__ == "__main__":
    app = SampleApp()  # create an instant from class SampleApp
    app.mainloop()

