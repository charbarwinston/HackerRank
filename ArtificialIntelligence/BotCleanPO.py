#!/usr/bin/python

import random

def next_move(posc, posr, board):
    if board[posc][posr] == 'd':
        print("CLEAN")
        return

    #down
    try:
        if board[posc+1][posr] == 'd':
            print("DOWN")
            return
    except:
        pass
    #up
    try:
        if board[posc-1][posr] == 'd':
            print("UP")
            return
    except:
        pass
    #right
    try:
        if board[posc][posr+1] == 'd':
            print("RIGHT")
            return
    except:
        pass
    #left
    try:
        if board[posc][posr-1] == 'd':
            print("LEFT")
            return
    except:
        pass
    #down Right
    try:
        if board[posc+1][posr + 1] == 'd':
            print("DOWN")
            return
    except:
        pass
    #up Right
    try:
        if board[posc-1][posr + 1] == 'd':
            print("UP")
            return
    except:
        pass
    #down Left
    try:
        if board[posc+1][posr-1] == 'd':
            print("DOWN")
            return
    except:
        pass
    #up left
    try:
        if board[posc - 1][posr-1] == 'd':
            print("UP")
            return
    except:
        pass 

    while True:
        try:
            rand = random.randint(1,4)
            if rand == 1:
                if board[posc - 1][posr]:
                    print("UP")
                    return
            elif rand == 2:
                if board[posc + 1][posr]:
                    print("DOWN")
                    return
            elif rand == 3:
                if board[posc][posr+1]:
                    print("RIGHT")
                    return
            elif rand == 4:
                if board[posc][posr-1]:
                    print("LEFT")
                    return
        except:
            pass

    


pos = [0,1]
board = [
            "-b---",
            "-----",
            "-----",
            "-d---",
            "-----",
        ]

next_move(pos[0], pos[1], board)
