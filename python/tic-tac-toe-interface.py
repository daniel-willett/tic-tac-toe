#!/usr/bin/python3

import tkinter as tk

root = tk.Tk()
root.title("Tic Tac Toe")

#Create 9 buttons
button00 = tk.Button(root)
button01 = tk.Button(root)
button02 = tk.Button(root)
button10 = tk.Button(root)
button11 = tk.Button(root)
button12 = tk.Button(root)
button20 = tk.Button(root)
button21 = tk.Button(root)
button22 = tk.Button(root)

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


