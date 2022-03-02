from tkinter import *
import tkinter_pg_2 as tp2

def loopingWindow():

    def destroyWindow():
        window.destroy()
        tp2.go()

    window = Tk()
    window.title("Welcome to LikeGeeks app")
    window.geometry('350x200')
    lbl = Label(window, text="Hello")
    lbl.grid(column=0, row=0)
    btn = Button(window, text="Click Me",  command=destroyWindow)
    btn.grid(column=1, row=0)
    window.mainloop()




