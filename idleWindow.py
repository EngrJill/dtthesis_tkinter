from tkinter import *
import systemProcesses as pro
import systemProcesses as sp

def loopingWindow():

    def proceedWindow():
        window.destroy()
        sp.process()
        

    window = Tk()
    window.title("Welcome to LikeGeeks app")
    window.geometry('350x200')
    lbl = Label(window, text="Hello")
    lbl.grid(column=0, row=0)
    btn = Button(window, text="Click Me",  command=proceedWindow)
    btn.grid(column=1, row=0)
    window.mainloop()






