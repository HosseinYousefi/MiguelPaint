from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from tool import *

root = Tk()
root.title('MiguelPaint 2020')

tools_frame = Frame(root, width=100, bg='#2c2c2c')
tools_frame.grid(row=0, column=0, rowspan=2, sticky=(N, S, W))

canvas = Canvas(root, width=720, height=720)
canvas.grid(row=0, column=1, sticky=(N, E, W, S))

last_pressed_x = 0
last_pressed_y = 0

stroke = 'black'
fill = 'white'

def register_press(e):
    global last_pressed_x, last_pressed_y
    last_pressed_x = e.x
    last_pressed_y = e.y

last_rectangle = None

def register_release(e):
    if last_rectangle:
        canvas.delete(last_rectangle)
    canvas.create_rectangle((last_pressed_x, last_pressed_y, e.x, e.y), fill=fill, outline=stroke)

def register_motion(e):
    global last_rectangle
    if last_rectangle:
        canvas.delete(last_rectangle)
    last_rectangle = canvas.create_rectangle((last_pressed_x, last_pressed_y, e.x, e.y), fill=fill, outline=stroke)

canvas.bind('<ButtonPress-1>', register_press)
canvas.bind('<ButtonRelease-1>', register_release)
canvas.bind('<Button1-Motion>', register_motion)



# Color picker

colors_frame = Frame(root, height=100, bg='#dcdcdc')
colors_frame.grid(row=1, column=1, sticky=(S, W, E))

stroke_label = Label(colors_frame, text='Stroke:', bg='#dcdcdc')
stroke_label.grid(row=0, column=0)

fill_label = Label(colors_frame, text='Fill:', bg='#dcdcdc')
fill_label.grid(row=2, column=0)

colors = ['red', 'green', 'blue', 'black', 'white', 'pink', 'magenta', 'brown', 'purple']

Frame(colors_frame, height=10).grid(row=1, column=0)

def change_stroke(c):
    global stroke
    stroke = c

def change_fill(c):
    global fill
    fill = c


stroke_colors = []
fill_colors = []

def make_lambda(clr, f):
    return lambda e: f(clr)
    
def show_stroke_picker():
    global stroke
    stroke = colorchooser.askcolor()[1]

def show_fill_picker():
    global fill
    fill = colorchooser.askcolor()[1]

for i, color in enumerate(colors):
    stroke_colors.append(Frame(colors_frame, bg=color, width=20, height=20))
    stroke_colors[-1].grid(row=0, column=i+1)
    fill_colors.append(Frame(colors_frame, bg=color, width=20, height=20))
    fill_colors[-1].grid(row=2, column=i+1)

    stroke_colors[-1].bind('<1>', make_lambda(color, change_stroke))
    fill_colors[-1].bind('<1>', make_lambda(color, change_fill))

stroke_button = Button(colors_frame, command=show_stroke_picker, text='Select color')
stroke_button.grid(row=0, column=len(colors)+2)

fill_button = Button(colors_frame, command=show_fill_picker, text='Select color')
fill_button.grid(row=2, column=len(colors)+2)

oval_button = ToolButton(tools_frame, 'oval.gif')
oval_button.grid(row=0, column=0)

pencil_button = ToolButton(tools_frame, 'pencil.gif')
pencil_button.grid(row=1, column=0)

text_button = ToolButton(tools_frame, 'text.gif')
text_button.grid(row=2, column=0)

root.mainloop() 