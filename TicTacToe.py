import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("780x620")
root.resizable(False, False)
root.configure(background="#507dbc")
tk.Wm.wm_title(root, "Tic Tac Toe")
a1 = tk.StringVar(root)
a2 = tk.StringVar(root)
a3 = tk.StringVar(root)
b1 = tk.StringVar(root)
b2 = tk.StringVar(root)
b3 = tk.StringVar(root)
c1 = tk.StringVar(root)
c2 = tk.StringVar(root)
c3 = tk.StringVar(root)
wint = tk.StringVar(root)
t = tk.StringVar(root)
turns = 9
x1,x2,x3,y1,y2,y3,z1,z2,z3 = 0,0,0,0,0,0,0,0,0
t.set("X")

def reset():
    global x1,x2,x3,y1,y2,y3,z1,z2,z3,turns
    a1.set("")
    a2.set("")
    a3.set("")
    b1.set("")
    b2.set("")
    b3.set("")
    c1.set("")
    c2.set("")
    c3.set("")
    wint.set("")
    x1,x2,x3,y1,y2,y3,z1,z2,z3 = 0,0,0,0,0,0,0,0,0

def win():

    if (x1 and x2 and x3 and y1 and y2 and y3 and z1 and z2 and z3 != ""):
        wint.set("     DRAW!!")

    #----- HORIZONTAL -----#
    if x1 and x2 and x3 != "":
        if x1 == x2 == x3:
            wint.set(" Win the player "+str(x1))

    if y1 and y2 and y3 != "":
        if y1 == y2 == y3:
            wint.set(" Win the player "+str(y1))
    if z1 and z2 and z3 != "":
        if z1 == z2 == z3:
            wint.set(" Win the player "+str(z1))

    #----- VERTICAL -----#
    if x1 and y1 and z1 != "":
        if x1 == y1 == z1:
            wint.set(" Win the player "+str(x1))
    if x2 and y2 and z2 != "":
        if x2 == y2 == z2:
            wint.set(" Win the player "+str(x2))
    if x3 and y3 and z3 != "":
        if x3 == y3 == z3:
            wint.set(" Win the player "+str(x3))

    if x1 and y2 and z3 != "":
        if x1 == y2 == z3:
            wint.set(" Win the player "+str(x1))
    if x3 and y2 and z1 != "":
        if x3 == y2 == z1:
            wint.set(" Win the player "+str(x3))

def change(x):
    global x1,x2,x3,y1,y2,y3,z1,z2,z3,turns
    if (x == 1) and (a1.get() == ""):
        if turns%2 == 0:
            a1.set("O")
            turns -= 1
            x1 = 2
            t.set("X")
            win()
        else:
            a1.set("X")
            turns -= 1
            x1=1
            t.set("O")
            win()

    elif x == 2 and (a2.get() == ""):
        if turns%2 == 0:
            a2.set("O")
            turns -= 1
            x2=2
            t.set("X")
            win()
        else:
            a2.set("X")
            turns -= 1
            x2=1
            t.set("O")
            win()

    elif x == 3 and (a3.get() == ""):
        if turns%2 == 0:
            a3.set("O")
            turns -= 1
            x3=2
            t.set("X")
            win()
        else:
            a3.set("X")
            turns -= 1
            x3=1
            t.set("O")
            win()

    elif x == 4 and (b1.get() == ""):
        if turns%2 == 0:
            b1.set("O")
            turns -= 1
            y1=2
            t.set("X")
            win()
        else:
            b1.set("X")
            turns -= 1
            y1=1
            t.set("O")
            win()

    elif x == 5 and (b2.get() == ""):
        if turns%2 == 0:
            b2.set("O")
            turns -= 1
            y2=2
            t.set("X")
            win()
        else:
            b2.set("X")
            turns -= 1
            y2=1
            t.set("O")
            win()

    elif x == 6 and (b3.get() == ""):
        if turns%2 == 0:
            b3.set("O")
            turns -= 1
            y3=2
            t.set("X")
            win()
        else:
            b3.set("X")
            turns -= 1
            y3=1
            t.set("O")
            win()

    elif x == 7 and (c1.get() == ""):
        if turns%2 == 0:
            c1.set("O")
            turns -= 1
            z1=2
            t.set("X")
            win()
        else:
            c1.set("X")
            turns -= 1
            z1=1
            t.set("O")
            win()

    elif x == 8 and (c2.get() == ""):
        if turns%2 == 0:
            c2.set("O")
            turns -= 1
            z2=2
            t.set("X")
            win()
        else:
            c2.set("X")
            turns -= 1
            z2=1
            t.set("O")
            win()

    elif x == 9 and (c3.get() == ""):
        if turns%2 == 0:
            c3.set("O")
            turns -= 1
            z3=2
            t.set("X")
            win()
        else:
            c3.set("X")
            turns -= 1
            z3=1
            t.set("O")
            win()

    else:
        pass


tk.Label(
    root,
    textvariable=t,
    font=("Courier",50,"bold"),
    bg="#507dbc",
    fg="white"
).place(x=670,y=130)

tk.Label(
    root,
    text="TURN:",
    font=("Courier",22,"bold"),
    bg="#507dbc",
    fg="white"
).place(x=560,y=150)

tk.Label(
    root,
    textvariable=wint,
    font=("Courier",50,"bold"),
    bg="#507dbc",
    fg="white"
).place(x=10,y=10)

tk.Label(
    root,
    text="Player 1 = X\nPlayer 2 = O",
    font=("Courier",20,"bold"),
    bg="#507dbc",
    fg="white"
).place(x=560,y=270)

tk.Button(
    root,
    textvariable=a1,
    font=("Courier",50,"bold"),
    bg="#1d3461",
    fg="white",
    width=3,
    height=1,
    bd=5,
    relief="solid",
    command=lambda: change(1)
).place(x=100,y=100)

tk.Button(
    root,
    textvariable=a2,
    font=("Courier",50,"bold"),
    bg="#1d3461",
    fg="white",
    width=3,
    height=1,
    bd=5,
    relief="solid",
    command=lambda: change(2)
).place(x=250,y=100)

tk.Button(
    root,
    textvariable=a3,
    font=("Courier",50,"bold"),
    bg="#1d3461",
    fg="white",
    width=3,
    height=1,
    bd=5,
    relief="solid",
    command=lambda: change(3)
).place(x=400,y=100)

tk.Button(
    root,
    textvariable=b1,
    font=("Courier",50,"bold"),
    bg="#1d3461",
    fg="white",
    width=3,
    height=1,
    bd=5,
    relief="solid",
    command=lambda: change(4)
).place(x=100,y=250)

tk.Button(
    root,
    textvariable=b2,
    font=("Courier",50,"bold"),
    bg="#1d3461",
    fg="white",
    width=3,
    height=1,
    bd=5,
    relief="solid",
    command=lambda: change(5)
).place(x=250,y=250)

tk.Button(
    root,
    textvariable=b3,
    font=("Courier",50,"bold"),
    bg="#1d3461",
    fg="white",
    width=3,
    height=1,
    bd=5,
    relief="solid",
    command=lambda: change(6)
).place(x=400,y=250)

tk.Button(
    root,
    textvariable=c1,
    font=("Courier",50,"bold"),
    bg="#1d3461",
    fg="white",
    width=3,
    height=1,
    bd=5,
    relief="solid",
    command=lambda: change(7)
).place(x=100,y=400)

tk.Button(
    root,
    textvariable=c2,
    font=("Courier",50,"bold"),
    bg="#1d3461",
    fg="white",
    width=3,
    height=1,
    bd=5,
    relief="solid",
    command=lambda: change(8)
).place(x=250,y=400)

tk.Button(
    root,
    textvariable=c3,
    font=("Courier",50,"bold"),
    bg="#1d3461",
    fg="white",
    width=3,
    height=1,
    bd=5,
    relief="solid",
    command=lambda: change(9)
).place(x=400,y=400)



tk.Button(
    root,
    text="RESET",
    font=("Courier",20,"bold"),
    bg="#a22c29",
    fg="white",
    width=8,
    height=2,
    bd=5,
    relief="solid",
    command=reset
).place(x=600,y=500)



tk.mainloop()