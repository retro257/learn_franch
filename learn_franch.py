from tkinter import *
import pandas
from random import *
import time

start = True
next = True
rand = 0
dat = pandas.read_csv("data/french_words.csv")
data = pandas.DataFrame(dat)
go = True


window = Tk()
window.title("Franch_learn")
window.geometry('830x530')

img1 = PhotoImage(file="images/card_front.png")
img2 = PhotoImage(file="images/card_back.png")
img_button_ok = PhotoImage(file="images/right.png")
img_button_notok = PhotoImage(file="images/wrong.png")
b = Label(image = img1, text=data["French"][rand], font=("Arial Bold", 50), compound="center")
def ok():
    global go
    b = Label(image = img1, text=data["English"][rand], font=("Arial Bold", 50), compound="center")
    b.grid(column=1, row=1)
    button_ok = Button(image=img_button_ok, command=click)
    button_ok.place(x=600, y=370)

    button_notok = Button(image=img_button_notok, command=click)
    button_notok.place(x=100, y=370)
    go = False

def click():
    global b
    global rand
    rand = randint(0, 100)
    b = Label(image = img2, text=data["French"][rand], font=("Arial Bold", 50), compound="center")
    b.grid(column=1, row=1)
    button_ok = Button(image=img_button_ok, command=click)
    button_ok.place(x=600, y=370)

    button_notok = Button(image=img_button_notok, command=click)
    button_notok.place(x=100, y=370)
    window.after(3000, ok)
    

flip_timer = window.after(3000, func=click)

button_ok = Button(image=img_button_ok, command=click)
button_ok.place(x=600, y=370)

button_notok = Button(image=img_button_notok, command=click)
button_notok.place(x=100, y=370)
    
    
window.mainloop()
    


