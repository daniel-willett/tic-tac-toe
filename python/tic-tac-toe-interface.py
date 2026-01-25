#!/usr/bin/python3

import tkinter as tk

def button_click(btnNum):
    btnLookup = {"00":button00,
              "01":button01,
              "02":button02,
              "10":button10,
              "11":button11,
              "12":button12,
              "20":button20,
              "21":button21,
              "22":button22
              }
    temp = btnLookup[btnNum]
    temp.config(text="X")

root = tk.Tk()
root.title("Tic Tac Toe")

#Create 9 buttons
button00 = tk.Button(root, command=lambda: button_click("00"))
button01 = tk.Button(root, command=lambda: button_click("01"))
button02 = tk.Button(root, command=lambda: button_click("02"))
button10 = tk.Button(root, command=lambda: button_click("10"))
button11 = tk.Button(root, command=lambda: button_click("11"))
button12 = tk.Button(root, command=lambda: button_click("12"))
button20 = tk.Button(root, command=lambda: button_click("20"))
button21 = tk.Button(root, command=lambda: button_click("21"))
button22 = tk.Button(root, command=lambda: button_click("22"))

button00.grid(row=0, column=0)
button01.grid(row=1, column=0)
button02.grid(row=2, column=0)
button10.grid(row=0, column=1)
button11.grid(row=1, column=1)
button12.grid(row=2, column=1)
button20.grid(row=0, column=2)
button21.grid(row=1, column=2)
button22.grid(row=2, column=2)

root.mainloop()


