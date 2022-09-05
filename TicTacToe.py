from tkinter import *
from math import inf as infinity
from random import choice
from tkinter import messagebox
HUMAN = -1
COMP = +1

root = Tk()
root.title('Tic Tac Toe IA')

def resetBoard():
    b1.destroy()
    b2.destroy()
    b3.destroy()
    b4.destroy()
    b5.destroy()
    b6.destroy()
    b7.destroy()
    b8.destroy()
    b9.destroy()
    introScene()

def resetSinglePlayer():
    sb1.destroy()
    sb2.destroy()
    sb3.destroy()
    sb4.destroy()
    sb5.destroy()
    sb6.destroy()
    sb7.destroy()
    sb8.destroy()
    sb9.destroy()
    introScene()

def checkWin():
    #Horizontal victory check
    for x in gameboard: 
        if x.count('o') == 3 or x.count('x') == 3:
            print("Player " + x[0] + " won the game")
            messagebox.showinfo("Game Over", "Player " + x[0] + " won the game")
            resetBoard()
      
    #Vertical victory Check
    for i in range(3):
        counterx = 0
        countero = 0
        for x in gameboard:
            if x[i] == "o":
                countero += 1
            if x[i] == "x":
                counterx += 1
            if countero == 3 or counterx == 3:
                print("Player " + x[i] + " won the game")
                messagebox.showinfo("Game Over", "Player " + x[i] + " won the game")
                resetBoard()
       
    #Diagonal Victory Check
    if gameboard [0][0] == "x" and gameboard[1][1] == "x" and gameboard [2][2] == "x":
        print("Player x won the game")
        messagebox.showinfo("Game Over", "Player x won the game")
        resetBoard()
    
    if gameboard [0][0] == "o" and gameboard[1][1] == "o" and gameboard [2][2] == "o":
        print("Player o won the game")
        messagebox.showinfo("Game Over", "Player o won the game")
        resetBoard()
    
    if gameboard [0][2] == "x" and gameboard[1][1] == "x" and gameboard [2][0] == "x":
        print("Player x won the game")
        messagebox.showinfo("Game Over", "Player x won the game")
        resetBoard()
    
    if gameboard [0][2] == "o" and gameboard[1][1] == "o" and gameboard [2][0] == "o":
        print("Player o won the game")
        messagebox.showinfo("Game Over", "Player o won the game")
        resetBoard()
    
    #Tie Check
    check = 0
    for x in gameboard:
        if x.count('x') + x.count('o') == 3:
            check += 1
        if check == 3:
            print("Tie Game")
            messagebox.showinfo("Game Over", "Tie Game")
            resetBoard()


#Button Clicked Function
def b_click(b):
    info = b.grid_info()
    x = info["row"]
    y = info["column"]

    global humanTurn
    if b["text"] == " " and humanTurn == True:
        b["text"] = "X"
        gameboard[x][y] = "x"
        humanTurn = False
        checkWin()
        
    elif b["text"] == " " and humanTurn == False:
        b["text"] = "O"
        gameboard[x][y] = "o"
        humanTurn = True
        checkWin()
    else:
        messagebox.showerror("Tic Tac Toe", "That box has already been selected")
        
def twoPlayerClick():
    welcomeLabel.destroy()
    twoPlayerButton.destroy()
    singlePlayerButton.destroy()
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    #Building buttons
    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

    #Gridding buttons to screen
    b1.grid(row = 0, column = 0)
    b2.grid(row = 0, column = 1)
    b3.grid(row = 0, column = 2)

    b4.grid(row = 1, column = 0)
    b5.grid(row = 1, column = 1)
    b6.grid(row = 1, column = 2)

    b7.grid(row = 2, column = 0)
    b8.grid(row = 2, column = 1)
    b9.grid(row = 2, column = 2)


def visualChange(x, y):
    info = sb1.grid_info()
    a = info["row"]
    b = info["column"]
    if (x, y) == (a, b):
        sb1["text"] = "O"
    info = sb2.grid_info()
    a = info["row"]
    b = info["column"]
    if (x, y) == (a, b):
        sb2["text"] = "O"
    info = sb3.grid_info()
    a = info["row"]
    b = info["column"]
    if (x, y) == (a, b):
        sb3["text"] = "O"
    info = sb4.grid_info()
    a = info["row"]
    b = info["column"]
    if (x, y) == (a, b):
        sb4["text"] = "O"
    info = sb5.grid_info()
    a = info["row"]
    b = info["column"]
    if (x, y) == (a, b):
        sb5["text"] = "O"
    info = sb6.grid_info()
    a = info["row"]
    b = info["column"]
    if (x, y) == (a, b):
        sb6["text"] = "O"
    info = sb7.grid_info()
    a = info["row"]
    b = info["column"]
    if (x, y) == (a, b):
        sb7["text"] = "O"
    info = sb8.grid_info()
    a = info["row"]
    b = info["column"]
    if (x, y) == (a, b):
        sb8["text"] = "O"
    info = sb9.grid_info()
    a = info["row"]
    b = info["column"]
    if (x, y) == (a, b):
        sb9["text"] = "O"

def evaluate(state):
    if wins(state, COMP):
        score = 1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score

def wins(state, player):
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False

def game_over(state):
    return wins(state, HUMAN) or wins(state, COMP)

def empty_cells(state):
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == " ":
                cells.append([x, y])

    return cells

def minimax(state, depth, player):
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = " "
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value
    return best

def ai_turn():
    depth = len(empty_cells(gameboard))
    move = minimax(gameboard, depth, COMP)
    x, y = move[0], move[1]
    gameboard[x][y] = COMP
    visualChange(x,y)

    if game_over(gameboard) or depth == 0:
        resetSinglePlayer()

#Singleplayer Button Clicked Function
def sb_click(sb):
    info = sb.grid_info()
    x = info["row"]
    y = info["column"]
    if sb["text"] == " ":
        sb["text"] = "X"
        gameboard[x][y] = HUMAN
        didwin = game_over(gameboard)
        if didwin:
            resetSinglePlayer()
        ai_turn()
    else:
        messagebox.showerror("Tic Tac Toe", "That box has already been selected")

    


def singlePlayerClick():
    welcomeLabel.destroy()
    twoPlayerButton.destroy()
    singlePlayerButton.destroy()
    
    global sb1, sb2, sb3, sb4, sb5, sb6, sb7, sb8, sb9
    #Building buttons
    sb1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: sb_click(sb1))
    sb2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: sb_click(sb2))
    sb3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: sb_click(sb3))
 
    sb4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: sb_click(sb4))
    sb5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: sb_click(sb5))
    sb6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: sb_click(sb6))
 
    sb7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: sb_click(sb7))
    sb8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: sb_click(sb8))
    sb9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: sb_click(sb9))
 
    #Gridding buttons to screen
    sb1.grid(row = 0, column = 0)
    sb2.grid(row = 0, column = 1)
    sb3.grid(row = 0, column = 2)
 
    sb4.grid(row = 1, column = 0)
    sb5.grid(row = 1, column = 1)
    sb6.grid(row = 1, column = 2)
 
    sb7.grid(row = 2, column = 0)
    sb8.grid(row = 2, column = 1)
    sb9.grid(row = 2, column = 2)

def introScene():
    #Creating 2D matrix to store x and y values
    global gameboard
    gameboard = [[" " for x in range(3)] for y in range(3)] 
    #Alternating Player Turn
    global humanTurn
    humanTurn = True
    
    #Creating Intro Scene
    global welcomeLabel
    welcomeLabel = Label(root, text="Welcome to Tic Tac Toe")
    global twoPlayerButton
    twoPlayerButton = Button(root, text="Two Players", padx=50, pady= 50, command=twoPlayerClick)
    global singlePlayerButton
    singlePlayerButton = Button(root, text="Single Player", padx=50, pady= 50, command=singlePlayerClick)

    #Positioning Intro Scene
    welcomeLabel.grid(row=0,column=0)
    twoPlayerButton.grid(row=1, column=0)
    singlePlayerButton.grid(row=1,column=1) 

introScene()


root.mainloop()