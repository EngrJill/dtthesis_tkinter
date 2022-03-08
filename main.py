import tkinter as tk
from scanAdminAccess import checkQrCodeAdmin as cqr
import idleWindow as iw

from tkinter.ttk import Progressbar
from tkinter import HORIZONTAL, ttk

def main():

    def write_slogan():
        print("Tkinter is easy to use!")

    root = tk.Tk()

    # Theme
    theme='#4d97fe'


    # Main window settings
    width_of_window = 427
    height_of_window = 250
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width/2)-(width_of_window/2)
    y_coordinate = (screen_height/2)-(height_of_window/2)
    root.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

    root.overrideredirect(1)

    # Main window's Frame Settings
    frame = tk.Frame(root,width=427,height=241,bg=theme).place(x=0,y=0)


    # Label
    l1=tk.Label(root,text='Integrated',fg='white',bg=theme)
    lst1=('Calibri (Body)',18,'bold')
    l1.config(font=lst1)
    l1.place(x=50,y=80)

    l2=tk.Label(root,text='RasPi Security',fg='white',bg=theme)
    lst2=('Calibri (Body)',18)
    l2.config(font=lst2)
    l2.place(x=170,y=82)

    l3=tk.Label(root,text='DREAMTEAM01',fg='white',bg=theme)
    lst3=('Calibri (Body)',13)
    l3.config(font=lst3)
    l3.place(x=50,y=110)


    # Progress Bar Style
    s = ttk.Style()
    s.theme_use('clam')
    s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
    progress=Progressbar(root,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate',)


    # Progress Bar Function
    def bar():

        l4=tk.Label(root,text='Loading...',fg='white',bg=theme)
        lst4=('Calibri (Body)',10)
        l4.config(font=lst4)
        l4.place(x=18,y=210)
        
        import time
        r=0
        for i in range(100):
            progress['value']=r
            root.update_idletasks()
            time.sleep(0.03)
            r=r+1
        
        root.destroy()
        if (cqr() == True):
            iw.loopingWindow()

        
            
    progress.place(x=-10,y=235)


    # Buttons
    button = tk.Button(frame, width=10, height=1, text="QUIT", fg="red", border=0, command=quit, bg='white')
    button.place(x=130,y=200)
    slogan = tk.Button(frame, width=10, height=1, text="SCAN QR", fg=theme, border=0, command=bar, bg='white')
    slogan.place(x=220,y=200)

    root.mainloop()


if __name__ == "__main__":
    main()