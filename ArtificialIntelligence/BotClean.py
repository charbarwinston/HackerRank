#!/usr/bin/python

from math import sqrt

import tkinter as tk

def updateLoop(root):
    def move():
        nextMove = next_move()
        if nextMove == "Clean":
            cleanTile()
        elif nextMove == "Right":
            moveRight()
        elif nextMove == "Left":
            moveLeft()
        elif nextMove == "Down":
            moveUp()
        elif nextMove == "Up":
            moveDown()
        updateBoard()
        root.after(1000, move())
    move()

def next_move():
    global pos
    posc = pos[0]
    posr = pos[1]
    global board
    if board[posc][posr] == 'd':
        return("CLEAN")
    closestPoint = []
    closestDistance = 999999999
    for y, row in enumerate(board):
        for rowIndex, char in enumerate(row):
            if char == 'd':
                disY = (y - posc)**2
                disX = (rowIndex - posr)**2
                distance = sqrt(disX + disY)
                if distance < closestDistance:
                    closestDistance = distance
                    closestPoint = [rowIndex,y]
    if closestPoint[0] > posr:
        return('RIGHT')
    elif closestPoint[0] < posr:
        return('LEFT')
    elif closestPoint[1] > posc:
        return('DOWN')
    elif closestPoint[1] < posc:
        return('UP')

def cleanTile():
    global pos
    global board
    board[pos[0]][pos[1]] = "b"

def moveRight():
    global pos
    global board
    board[pos[0]][pos[1]] = "-"
    if board[pos[0] + 1][pos[1]] != "d":
        board[pos[0] + 1][pos[1]] = "b"
    pos = [pos[0] + 1, pos[1]]

def moveLeft():
    global pos
    global board
    board[pos[0]][pos[1]] = "-"
    if board[pos[0] - 1][pos[1]] != "d":
        board[pos[0] - 1][pos[1]] = "b"
    pos = [pos[0] - 1, pos[1]]

def moveDown():
    global pos
    global board
    board[pos[0]][pos[1]] = "-"
    if board[pos[0]][pos[1] + 1] != "d":
        board[pos[0]][pos[1] + 1] = "b"
    pos = [pos[0], pos[1] + 1]

def moveUp():
    global pos
    global board
    board[pos[0]][pos[1]] = "-"
    if board[pos[0]][pos[1] - 1] != "d":
        board[pos[0]][pos[1] - 1] = "b"
    pos = [pos[0], pos[1] - 1]

def initializeBoard(board, root):
    labels = {}
    for i, row in enumerate(board):
        for ci, char in enumerate(row):
            if i not in labels:
                labels[i] = []
            if char == 'b':
                labels[i].append(tk.Label(root, bg="blue", width=10, height=5))
                labels[i][ci].grid(row=i,column=ci)
            elif char == 'd':
                labels[i].append(tk.Label(root, bg="brown", width=10, height=5))
                labels[i][ci].grid(row=i,column=ci)
            elif char == '-':
                labels[i].append(tk.Label(root, bg="gray", width=10, height=5))
                labels[i][ci].grid(row=i,column=ci)
    return(labels)


def updateBoard():
    global board
    global labels
    for i, row in enumerate(board):
        for ci, char in enumerate(row):
            if char == 'b':
                labels[i][ci].configure(bg="blue")
            elif char == 'd':
                labels[i][ci].configure(bg="brown")
            elif char == '-':
                labels[i][ci].configure(bg="gray")

pos = [0,1]
board = [
        "bd---",
        "-d---",
        "---d-",
        "--d--",
        "----d"
        ]
#next_move(pos[0], pos[1], board)

root = tk.Tk()
root.title("BotClean")
labels = initializeBoard(board,root)
updateLoop(root)
root.mainloop()
