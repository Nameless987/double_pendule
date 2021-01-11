from tkinter import *
from random import *

import math

fenetre=Tk()
cnv=Canvas(fenetre, width=600, height=400, bg="black")
cnv.pack(padx=5, pady=5)

def create_circle(x, y, r,cnv, color):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return cnv.create_oval(x0, y0, x1, y1, fill = color)

g = 0.25
pi = 3.14159265358
r1 = 85
r2 = 85
m1 = 1
m2 = 1
a = randint(70, 110)
b = randint(70, 110)
a1 = math.radians(90+a)
a2 = math.radians(90+b)
px2 = 305 + r1*math.sin(a1)+ r2*math.sin(a2)
py2 = 205 + r1*math.cos(a1)+ r2*math.cos(a2)
a1_v = 0
a2_v  = 0
a1_a = 0
a2_a  = 0
p0 = create_circle(305, 205, 5,cnv, "magenta")
p1 = create_circle(305, 205, 5,cnv, "magenta")
p2 = create_circle(305, 205, 5,cnv, "magenta")
p3 = create_circle(305, 205, 5,cnv, "magenta")
l1 = cnv.create_line(305, 205, 0, 0, fill = "white")
l2 = cnv.create_line(305, 205, 0, 0, fill = "white")
l3 = cnv.create_line(305, 205, 0, 0, fill = "white")
cnv.delete(l3)


def deplacement():
    global a1, a2, a1_v, a2_v, a1_a, a2_a
    global p0, p1, p2, p3
    global px2, py2
    global l1, l2, l3
    global r1, r2
    global g, m1, m2

    num1 = -g * (2 * m1 + m2) * math.sin(a1)
    num2 = -m2 * g * math.sin(a1 - (2*a2))
    num3 = -2 * math.sin(a1 - a2) * m2
    num4 = a2_v * a2_v * r2 + a1_v * a1_v * r1 * math.cos(a1 - a2)
    den = r1 * (2 * m1 + m2 - m2 * math.cos((2*a1) - (2*a2)))
    a1_a = (num1 + num2 + (num3*num4)) / den

    num1 = 2 * math.sin(a1 - a2)
    num2 = a1_v * a1_v * r1 * (m1 + m2)
    num3 = g * (m1 + m2) * math.cos(a1)
    num4 = a2_v * a2_v * r2 * m2 * math.cos(a1 - a2)
    den = r2 * ((2*m1) + m2 - (m2*math.cos(2 * a1 - 2 * a2)))
    a2_a = (num1 * (num2 + num3 + num4)) / den

    a1_v += a1_a
    a2_v += a2_a
    a1 += a1_v
    a2 += a2_v

    x1 = 305 + r1*math.sin(a1)
    y1 = 205 + r1*math.cos(a1)
    x2 = x1 + r2*math.sin(a2)
    y2 = y1 + r2*math.cos(a2)

    l3 = cnv.create_line(px2, py2, x2, y2,fill = "orange")

    px2 = x2
    py2 = y2

    cnv.delete(p1)
    cnv.delete(p2)
    cnv.delete(p3)
    cnv.delete(l1)
    cnv.delete(l2)
    p1 = create_circle(x1, y1, 5,cnv, "magenta")
    p3 = create_circle(x2, y2, 2, cnv, "orange")
    p2 = create_circle(x2, y2, 5, cnv, "magenta")
    l1 = cnv.create_line(305, 205, (cnv.coords(p1)[0]+5),(cnv.coords(p1)[1]+5), fill = "green")
    l2 = cnv.create_line((cnv.coords(p1)[0]+5),(cnv.coords(p1)[1]+5), (cnv.coords(p2)[0]+5),(cnv.coords(p2)[1]+5), fill = "green")
    cnv.delete(p1)
    cnv.delete(p2)
    cnv.delete(p3)
    p1 = create_circle(x1, y1, 5,cnv, "magenta")
    p3 = create_circle(x2, y2, 2, cnv, "orange")
    p2 = create_circle(x2, y2, 5, cnv, "magenta")
    fenetre.after(15, deplacement)

deplacement()
    
fenetre.mainloop()