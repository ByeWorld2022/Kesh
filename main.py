from sqlite3 import Cursor
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk
from turtle import color
import pyautogui
import os

root = Tk()
root.title("White Board")
root.overrideredirect(True)
root.geometry("80x430+150+50")
root.configure(bg="#f2f3f5")
root.resizable(False,False)
#root.wm_attributes('-topmost', True)
#root.wm_attributes('-transparentcolor','#add123')

pen_on=False
mag=False
current_x = 0
current_y = 0
color = 'black'

def annotate():
    global pen_on
    if pen_on==False:

        os.system("cmd /k screenpen")

def magnify():
    pass

def zoomify():
    pass

def voice():
    pass


def clearall():
    root.destroy()

def locate_xy(work):
    global current_x, current_y

    current_x = work.x
    current_y = work.y


def show_color(new_color):
    global color
    color=new_color


#icon



mag_icon=PhotoImage(file="./icons/mag.png")
Button(root,image=mag_icon,bg="#f2f3f5",command=magnify).place(x=20,y=50)

zoom_icon=PhotoImage(file="./icons/zoom.png")
Button(root,image=zoom_icon,bg="#f2f3f5",command=zoomify).place(x=20,y=90)

pen_icon=PhotoImage(file="./icons/pen1.png")
Button(root,image=pen_icon,bg="#f2f3f5",command=annotate).place(x=20,y=130)

destroy=PhotoImage(file="./icons/destroy.png")
Button(root,image=destroy,bg="#f2f3f5",command=clearall).place(x=20,y=370)

voice_icon=PhotoImage(file="./icons/voice.png")
Button(root,image=voice_icon,bg="#f2f3f5",command=annotate).place(x=20,y=10)



colors=Canvas(root,bg="#ffffff",width=37,height=190,bd=0)
colors.place(x=18,y=160)


def display_palette():
    id=colors.create_rectangle((10,10,30,30),fill="black")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('black'))

    id=colors.create_rectangle((10,40,30,60),fill="gray")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('gray'))

    id=colors.create_rectangle((10,70,30,90),fill="yellow")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('yellow'))

    id=colors.create_rectangle((10,100,30,120),fill="green")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('green'))

    id=colors.create_rectangle((10,130,30,150),fill="blue")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('blue'))

    id=colors.create_rectangle((10,160,30,180),fill="red")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('red'))

    
display_palette()




#slider
current_value=tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())


slider=ttk.Scale(root, from_=0,to=100,orient='horizontal',command=slider_changed,variable=current_value)
slider.place(x=30,y=580)

#value label
value_label=ttk.Label(root,text=get_current_value())
value_label.place(x=21,y=560)



root.mainloop()