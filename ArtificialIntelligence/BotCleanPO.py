#!/usr/bin/python

import random

def next_move(posc, posr, board):
    # if board[posc][posr] == 'd':
    #     print("CLEAN")
    #     return
    updateMemory(board)

def updateMemory(board):
    filename = "feedback.txt"
    f0 = 0
    try:
        f = open(filename, "x")
        fbBoard = board
        fbBoardOut = ""
        for i in range(5):
            for j in range(5):
             fbBoardOut = fbBoardOut + fbBoard[i][j]
            fbBoardOut = fbBoardOut + '\n'
        f.write(fbBoardOut)
        return
    except FileExistsError:
        f0 = 1
        f = open(filename, "r")
        fbBoard = [j for j in f.read().split('\n')]
        fbBoardList = []
        for i in range(len(fbBoard)):
            fbBoardList.append(list(fbBoard))
        f.close()
        f = open(filename, "w")
        for i in range(5):
            for j in range(5):
                if list(fbBoardList[i])[j] == 'o':
                    fbBoardList[i][j] = board[i][j]
    fbBoardOut = ""
    for i in range(5):
        for j in range(5):
            fbBoardOut = fbBoardList[i][j]
        fbBoardOut = fbBoardOut + '\n'
    f.write(fbBoardOut)
    f.close()

def lookForD(posc, posr, board):
    try:
        if board[posc+1][posr] == 'd':
            return("DOWN")
    except:
        pass
    try:
        if board[posc-1][posr] == 'd':
            return("UP")
    except:
        pass
    try:
        if board[posc][posr+1] == 'd':
            return("RIGHT")
    except:
        pass
    try:
        if board[posc][posr-1] == 'd':
            return("LEFT")
    except:
        pass
    try:
        if board[posc+1][posr + 1] == 'd':
            return("DOWN")
    except:
        pass
    try:
        if board[posc-1][posr + 1] == 'd':
            return("UP")
    except:
        pass
    try:
        if board[posc+1][posr-1] == 'd':
            return("DOWN")
    except:
        pass
    try:
        if board[posc - 1][posr-1] == 'd':
            return("UP")
    except:
        pass 

pos = [0,1]
board = [
            "-b--o",
            "---oo",
            "ooooo",
            "ooooo",
            "ooooo",
        ]

next_move(pos[0], pos[1], board)
