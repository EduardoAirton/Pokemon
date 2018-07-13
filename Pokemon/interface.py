#Eduardo Airton

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


    #Dropdown Menu
    POKEMONS = ["Fogo","Agua","Eletrico","Grama","Gelo"]

    variable = StringVar(master)
    variable.set(POKEMONS[0]) # valor default

    menu = OptionMenu(master, variable, *POKEMONS)
    menu.pack()
