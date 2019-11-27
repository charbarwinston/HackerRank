#!/usr/bin/python

from math import sqrt

def next_move(posc, posr, board):
    if board[posc][posr] == 'd':
        print("CLEAN")
        return

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
        print('RIGHT')
        return
    elif closestPoint[0] < posr:
        print('LEFT')
        return
    elif closestPoint[1] > posc:
        print('DOWN')
        return
    elif closestPoint[1] < posc:
        print('UP')
        return




pos = [0,0]
board = [
        ("bd---"),
        ("-d---"),
        ("---d-"),
        ("--d--"),
        ("----d")
        ]

next_move(pos[0], pos[1], board)
