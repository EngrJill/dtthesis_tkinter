#import QrDataBase as qrdb
from tkinter import *

def tempCheck():

    window = Tk()
    window.title("Welcome to LikeGeeks app")
    window.geometry('350x200')
    lbl = Label(window, text="Please Scan the QR Code")
    lbl.place(x=5, y=5)
    lbl2 = Label(window, text="Your QR Code is Accepted")
    lbl3 = Label(window, text="Your QR Code is Denied")

    temp = input("Please input temp in the terminal")

    if float(temp) < 37.5:
        lbl2.place(x=5, y=55)
    else:
        lbl3.place(x=5, y=55)

    window.mainloop()



    