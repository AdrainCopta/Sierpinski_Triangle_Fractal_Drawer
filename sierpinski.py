'''
Sierpinski triangle
'''

from tkinter import *
from math import *

def midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def draw_helper(canvas, level, p1, p2, p3):
    if level == 1:
        canvas.create_polygon(p1, p2, p3)
    else:
        p4 = midpoint(p1, p2);
        p5 = midpoint(p2, p3);
        p6 = midpoint(p1, p3);
        draw_helper(canvas, level - 1, p1, p4, p6);
        draw_helper(canvas, level - 1, p4, p2, p5);
        draw_helper(canvas, level - 1, p6, p5, p3);

class App:
    def __init__(self, master):
        master.title("Sierpinski Triangle Fractal")
        frame = Frame(master)
        frame.pack()

        self.size =500
        self.canvas = Canvas(frame, width=self.size, height=self.size, bg="cyan")
        self.canvas.pack(side=TOP)

        self.drawb = Button(frame, text="Draw", command=self.draw)
        self.drawb.pack(side=LEFT)

        w = Label(frame, text="Level")
        w.pack(side=LEFT)

        self.level = Entry(frame, width=3, justify=CENTER)
        self.level.insert(INSERT, "0")
        self.level.pack(side=LEFT)

    def draw(self):
        level = int(self.level.get())
        self.canvas.create_rectangle(0, 0, self.size + 5, self.size + 5, fill="cyan")
        triangle_height = int(round(self.size * sqrt(3.0) / 2.0))
        p1 = (2, triangle_height + 3)
        p2 = (2 + self.size / 2, 3)
        p3 = (2 + self.size, triangle_height + 3)
        draw_helper(self.canvas, level, p1, p2, p3)

root = Tk()
app = App(root)
root.mainloop()