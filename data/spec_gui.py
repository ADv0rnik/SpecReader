import tkinter as tk


class BaseInterface:
    def __init__(self):
        pass

root = tk.Tk()
root.title('SpecReader 0.9.1')

canvas = tk.Canvas(root, width= 800, height=600)
canvas.grid(columnspan = 3, rowspan = 3)

description = tk.Label(root, text='Browse spectrum file', font = 'Raleway')
description.grid(column = 0, row=0)
root.mainloop()