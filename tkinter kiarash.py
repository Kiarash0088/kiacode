import tkinter as tk
import turtle 
from tkinter import *
from PIL import ImageTk, Image

main_pg = tk.Tk()
main_pg.geometry('1180x400')
main_pg.title("my project")
main_pg.configure(bg="white")

def x () :
    wn = turtle.Screen()
    wn.bgpic("sodapdf-converted.gif")
    t = turtle.Turtle()
    t.penup()
    t.goto(0,-320)
    t.pendown()
    t.lt(90)
    t.fd(200)
bt1=tk.Button(
    width=15,
    height=7,
    bg="green",
    text="901",
    fg='white',
    command = x()
    )
bt2=tk.Button(
    width=15,
    height=7,
    bg="dark red",
    text= "انتشارات ",
    fg='white',
    command = x()
    )
bt3=tk.Button(
    width=15,
    height=7,
    bg="dark red",
    text="دفتر مديريت",
    fg='white',
    command = x()
    )
bt4=tk.Button(
    width=15,
    height=7,
    bg="dark red",
    text="دفتر معاونت انظباطي",
    fg='white',
    command = x()
    )
bt5=tk.Button(
    width=15,
    height=7,
    bg="dark red",
    text="دفتر پژوهشي",
    fg='white',
    command = x()
    )
bt6=tk.Button(
    width=15,
    height=7,
    bg= "dark red",
    text="سالن کنفرانس شهيد حامد رحيم پور ",
    fg='white',
    command = x()
    )
bt7=tk.Button(
    width=15,
    height=7,
    bg="dark red",
    text="انبار تربيت بدني " ,
    fg='white',
    command = x()
    )
image = Image.open("sodapdf-converted.gif")

resize_image = image.resize((600, 400))

img = ImageTk.PhotoImage(resize_image)

label1 = Label(image=img)
label1.image = img
label1.grid(row=0, column=0)

bt1.grid(row=0, column=1)
bt2.grid(row=0, column=2)
bt3.grid(row=0, column=3)
bt4.grid(row=0, column=4)
bt5.grid(row=0, column=5)
bt6.grid(row=0, column=6)
bt7.grid(row=0, column=7)
