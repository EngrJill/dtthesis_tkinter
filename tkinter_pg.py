import tkinter as tk
import tkinter_pg_2 as tp
import cv2


def main():

    def write_slogan():
        print("Tkinter is easy to use!")

    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    button = tk.Button(frame, text="QUIT", fg="red", command=quit)
    button.pack(side=tk.LEFT)
    slogan = tk.Button(frame, text="Go", command=tp.go)
    slogan.pack(side=tk.LEFT)

    root.mainloop()


if __name__ == "__main__":
    main()