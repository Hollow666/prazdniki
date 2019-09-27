import tkinter as tk
from tkinter import *
from tkinter import Button
from tkinter import Message
from tkinter import Label
from tkinter import Entry


def App():
    root = tk.Tk()
    root.title('Православные праздники')
    root.geometry('400x450')


    ### Elements
    input = Entry(root, font="Arial 10")
    label_year = Label(root, text='Введите год:', font="Arial 10", justify=LEFT)
    button = Button(root, text='Рассчитать', font="Arial 10", command=main())
    label_raznost = Label(root, text='Разность между календарями: {}', font="Arial 10", justify=LEFT)
    label_UK = Label(root, text='Юлианский календарь:', font="Arial 10 bold", justify=LEFT)
    label_PU = Label(root, text='Пасха: {}', font="Arial 10", justify=LEFT)
    label_VERB_U = Label(root, text='Вербное воскресенье: {}', font="Arial 10", justify=LEFT)
    label_VOZ_U = Label(root, text='Вознесение Христа: {}', font="Arial 10", justify=LEFT)
    label_TR_U = Label(root, text='Троица: {}', font="Arial 10", justify=LEFT)
    label_DS_U = Label(root, text='День Святого Духа: {}', font="Arial 10", justify=LEFT)
    label_GK = Label(root, text='Григорианский календарь:', font="Arial 10 bold", justify=LEFT)
    label_PG = Label(root, text='Пасха: {}', font="Arial 10", justify=LEFT)
    label_VERB_G = Label(root, text='Вербное воскресенье: {}', font="Arial 10", justify=LEFT)
    label_VOZ_G = Label(root, text='Вознесение Христа: {}', font="Arial 10", justify=LEFT)
    label_TR_G = Label(root, text='Троица: {}', font="Arial 10", justify=LEFT)
    label_DS_G = Label(root, text='День Святого Духа: {}', font="Arial 10", justify=LEFT)
    ###


    ### Packing
    input.pack()
    label_year.pack()
    button.pack()
    label_raznost.pack()
    label_UK.pack()
    label_PU.pack()
    label_VERB_U.pack()
    label_VOZ_U.pack()
    label_TR_U.pack()
    label_DS_U.pack()
    label_GK.pack()
    label_PG.pack()
    label_VERB_G.pack()
    label_VOZ_G.pack()
    label_TR_G.pack()
    label_DS_G.pack()
    ###


    input.place(x=120, y=13)
    label_year.place(x=20, y=10)
    button.place(x=280, y=9)
    label_raznost.place(x=20, y=50)
    label_UK.place(x=20, y=80)
    label_PU.place(x=30, y=110)
    label_VERB_U.place(x=30, y=140)
    label_VOZ_U.place(x=30, y=170)
    label_TR_U.place(x=30, y=200)
    label_DS_U.place(x=30, y=230)
    label_GK.place(x=20, y=260)
    label_PG.place(x=30, y=290)
    label_VERB_G.place(x=30, y=320)
    label_VOZ_G.place(x=30, y=350)
    label_TR_G.place(x=30, y=380)
    label_DS_G.place(x=30, y=410)


    root.mainloop()
    print(1)

def main():

    return


if __name__ == '__main__':
    App()