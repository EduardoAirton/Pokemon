from tkinter import *
from Main import *


def callback():
    print ("Click!")

if __name__ == '__main__':
    master = Tk()
    master.minsize(500, 350)
    c = Label(master,text="Digite tal coisa")

    c.pack()
    mainloop()
