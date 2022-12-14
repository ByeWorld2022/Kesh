from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk
from turtle import color

root = Tk()
root.title("White Board")
root.geometry("1050x600+150+50")
root.configure(bg="#f2f3f5")
root.resizable(False,False)
#root.wm_attributes('-topmost', True)
#root.wm_attributes('-transparentcolor','#add123')

undo_stack = []
redo_stack = []
stk = []
current_x = 0
current_y = 0
color = 'black'


def locate_xy(work):
    global current_x, current_y

    current_x = work.x
    current_y = work.y

def addLine(work):
    canvas.delete('temp_line_objects')
    global current_x, current_y, stack

    var = canvas.create_line((current_x,current_y,work.x,work.y),width=get_current_value(),fill=color,capstyle=ROUND,smooth=TRUE)
    stk.append((current_x,current_y,work.x,work.y,get_current_value(),color))
    current_x,current_y = work.x,work.y
    undo_stack.append(var)


def show_color(new_color):
    global color
    color=new_color

def new_canvas():
    canvas.delete('all')
    display_palette

def undo():
    global undo_stack, redo_stack, stk
    l=10
    while undo_stack and l>0:
        var = undo_stack.pop()
        canvas.delete(var)

        info = stk.pop()
        redo_stack.append(info)

        l=l-1
    display_palette

def redo():
    global undo_stack, redo_stack
    l=10
    while redo_stack and l>0:
        info = redo_stack.pop()
        var = canvas.create_line((info[0],info[1],info[2],info[3]),width=info[4],fill=info[5],capstyle=ROUND,smooth=True)

        undo_stack.append(var)
        stk.append(info)
        l=l-1
    display_palette 

#icon
image_icon=PhotoImage(file="./icons/paintbrush.png")
root.iconphoto(False,image_icon)

color_box=PhotoImage(file="./icons/color section.png")
Label(root,image=color_box,bg="#f2f3f5").place(x=7,y=17)

eraser=PhotoImage(file="./icons/eraser.png")
Button(root,image=eraser,bg="#f2f3f5",command=new_canvas).place(x=30,y=400)

undoButton = PhotoImage(file="./icons/undo.png")
Button(root,image=undoButton,bg="#f2f3f5",command=undo).place(x=30,y=450)

redoButton = PhotoImage(file="./icons/redo.png")
Button(root,image=redoButton,bg="#f2f3f5",command=redo).place(x=30,y=500)

canvas= Canvas(root,width=930,height=540,background="white",cursor="hand2")
canvas.place(x=100,y=10)
colors=Canvas(root,bg="#ffffff",width=37,height=310,bd=0)
colors.place(x=30,y=60)

def display_palette():
    id=colors.create_rectangle((10,10,30,30),fill="black")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('black'))

    id=colors.create_rectangle((10,40,30,60),fill="gray")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('gray'))

    id=colors.create_rectangle((10,70,30,90),fill="brown")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('brown'))

    id=colors.create_rectangle((10,100,30,120),fill="pink")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('pink'))

    id=colors.create_rectangle((10,130,30,150),fill="red")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('orange'))

    id=colors.create_rectangle((10,160,30,180),fill="yellow")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('yellow'))

    id=colors.create_rectangle((10,190,30,210),fill="green")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('green'))

    id=colors.create_rectangle((10,220,30,240),fill="blue")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('blue'))

    id=colors.create_rectangle((10,250,30,270),fill="red")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('red'))

    id=colors.create_rectangle((10,280,30,300),fill="white")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('white'))
    
display_palette()

canvas.bind('<Button-1>',locate_xy)
canvas.bind('<B1-Motion>',addLine)


#slider
current_value=tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())


slider=ttk.Scale(root, from_=0,to=100,orient='horizontal',command=slider_changed,variable=current_value)
slider.place(x=30,y=560)

#value label
value_label=ttk.Label(root,text=get_current_value())
value_label.place(x=27,y=580)



root.mainloop()
