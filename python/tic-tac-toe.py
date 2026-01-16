#!/usr/bin/python3
import re

def setup():
    for i in range(3):
        temp = []
        for j in range(3):
            temp.append(0)
        grid.append(temp)

def display():
    for i in range(3):
        print(str(3-i)+" "+str(grid[i]))
    print("   A  B  C")

def interpretInput(usrInput):
    lookup = {"A":0,
              "B":1,
              "C":2}
    usrInput = usrInput.replace(" ","")
    match = re.search("^[A-C][,-;:_]*[1-3]$", usrInput)
    if match==None:
        return -1
    char = (re.search("[A-C]",usrInput)).group()
    x = lookup[char]
    y = int((re.search("[1-3]", usrInput)).group())-1 #Arrays start at 0
    y = 2-y #The display is in reverse order to the `grid` indexing
    return [x,y]

def makeMove(position):
    global player
    x = position[0]
    y = position[1]
    if grid[y][x]!=0:
        print("This position is already taken. Please choose an empty position")
        player -= 1 #The next step is to increment it to the next player but we want the current player to try again
    else:
        grid[y][x]=player
        #Also need something else like an actual move being 'played' so perhaps just combine? That's a future problem. For now we work on `isLegal`

def hasWon():
    #Use an idea like in https://github.com/daniel-willett/project-euler/blob/main/python/q11.py


#Initialise
grid = []
"""
3 [0, 0, 0]
2 [0, 0, 0]
1 [0, 0, 0]
   A  B  C
"""
gameOver = False
player = 1


setup()
while gameOver==False:
    display()
    print("Player "+str(player)+"'s turn:")
    usrInput = input("where would you like to place?\n")
    position = interpretInput(usrInput)
    if position==-1:
        print("======Invalid input======")
    else:
        makeMove(position)
        player = (player%2)+1 #Switch between (0,1) but scaled by 1 so switch between (1,2)
        if hasWon()==True:
            gameOver=True
