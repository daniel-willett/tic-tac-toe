#!/usr/bin/python3

import tkinter as tk

def setup():
    for i in range(3):
        temp = []
        for j in range(3):
            temp.append(0)
        grid.append(temp)

def hasWon():
    #Use an idea like in https://github.com/daniel-willett/project-euler/blob/main/python/q11.py
    #2 in binary is 10
    #1 in binary is 01
    #0 in binary is 00
    #So we can take bitwise logical comparisons
    def northEast(x,y):
        if x>len(grid[0])-3:
            return 0
        if y<3-1:
            return 0
        return grid[y][x] & grid[y-1][x+1] & grid[y-2][x+2]

    def east(x,y):
        if x>len(grid[0])-3:
            return 0
        return grid[y][x] & grid[y][x+1] & grid[y][x+2]

    def southEast(x,y):
        if x>len(grid[0])-3:
            return 0
        if y>len(grid)-3:
            return 0
        return grid[y][x] & grid[y+1][x+1] & grid[y+2][x+2]

    def south(x,y):
        if y>len(grid)-3:
            return 0
        return grid[y][x] & grid[y+1][x] & grid[y+2][x]

    #Go through the whole playing field
    for i in range(3):
        for j in range(3):
            if northEast(i,j)!=0 or east(i,j)!=0 or southEast(i,j)!=0 or south(i,j)!=0:
                return True
    #Otherwise...
    return False

def button_click(btnNum):
    global player
    global gameOver
    if gameOver==False:

        x = int(btnNum[0])
        y = int(btnNum[1])

        if grid[y][x]!=0:
            print("This position is already taken. Please choose an empty position")
            player -= 1
        else:
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
            playChar = {1:"X", 2:"O"}
            temp = btnLookup[btnNum]
            temp.config(text=playChar[player])
            grid[y][x] = player

        player = (player%2)+1
        if hasWon()==True:
            gameOver=True
            print("Player "+str(playChar[player])+" has won!")
    else:
        pass


gameOver = False
player = 1
grid = []
setup()




















root = tk.Tk()
root.title("Tic Tac Toe")

btn_opts = {"width":4, "height":2, "font":("Arial", 36)}

#Create 9 buttons
button00 = tk.Button(root, **btn_opts, command=lambda: button_click("00"))
button01 = tk.Button(root, **btn_opts, command=lambda: button_click("01"))
button02 = tk.Button(root, **btn_opts, command=lambda: button_click("02"))
button10 = tk.Button(root, **btn_opts, command=lambda: button_click("10"))
button11 = tk.Button(root, **btn_opts, command=lambda: button_click("11"))
button12 = tk.Button(root, **btn_opts, command=lambda: button_click("12"))
button20 = tk.Button(root, **btn_opts, command=lambda: button_click("20"))
button21 = tk.Button(root, **btn_opts, command=lambda: button_click("21"))
button22 = tk.Button(root, **btn_opts, command=lambda: button_click("22"))

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


