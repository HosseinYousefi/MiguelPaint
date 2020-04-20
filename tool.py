from tkinter import *

class ToolButton(Button):
    def __init__(self, master, image_path):
        self.img = PhotoImage(file=image_path)
        self.img = self.img.subsample(16)
        super().__init__(master, image=self.img, highlightbackground='#2c2c2c', borderwidth=0)
        self.bind('<Enter>', self.enter)
        self.bind('<Leave>', self.leave)

    def enter(self, e):
        self['highlightbackground'] = '#111111'


    def leave(self, e):
        self['highlightbackground'] = '#2c2c2c'
