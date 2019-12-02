#!/usr/bin/python

from math import sqrt

def next_move(posc, posr, board):
    if board[posc][posr] == 'd':
        print("CLEAN")
        return

    closestPoint = []
    closestDistance = 999999999
    for y, row in enumerate(board):
        for x, char in enumerate(row):
            if char == 'd':
                disY = (y - posc)**2
                disX = (x - posr)**2
                distance = sqrt(disX + disY)
                if distance < closestDistance:
                    closestDistance = distance
                    closestPoint = [x,y]
                elif distance == closestDistance:
                    neighborsA = 0
                    neighborsB = 0
                    #down
                    try:
                        if board[y+1][x] == 'd':
                            neighborsB += 1
                        if board[closestPoint[1]+1][closestPoint[0]] == 'd':
                            neighborsA += 1
                    except:
                        pass
                    #up
                    try:
                        if board[y-1][x] == 'd':
                            neighborsB += 1
                        if board[closestPoint[1]-1][closestPoint[0]] == 'd':
                            neighborsA += 1
                    except:
                        pass
                    #right
                    try:
                        if board[y][x+1] == 'd':
                            neighborsB += 1
                        if board[closestPoint[1]][closestPoint[0]+1] == 'd':
                            neighborsA += 1
                    except:
                        pass
                    #left
                    try:
                        if board[y][x-1] == 'd':
                            neighborsB += 1
                        if board[closestPoint[1]][closestPoint[0]-1] == 'd':
                            neighborsA += 1
                    except:
                        pass
                    #down Right
                    try:
                        if board[y+1][x + 1] == 'd':
                            neighborsB += 1
                        if board[closestPoint[1]+1][closestPoint[0] + 1] == 'd':
                            neighborsA += 1
                    except:
                        pass
                    #up Right
                    try:
                        if board[y-1][x + 1] == 'd':
                            neighborsB += 1
                        if board[closestPoint[1]-1][closestPoint[0] + 1] == 'd':
                            neighborsA += 1
                    except:
                        pass
                    #down Left
                    try:
                        if board[y+1][x-1] == 'd':
                            neighborsB += 1
                        if board[closestPoint[1] + 1][closestPoint[0]-1] == 'd':
                            neighborsA += 1
                    except:
                        pass
                    #up left
                    try:
                        if board[y - 1][x-1] == 'd':
                            neighborsB += 1
                        if board[closestPoint[1] - 1][closestPoint[0]-1] == 'd':
                            neighborsA += 1
                    except:
                        pass                    
                    
                    if neighborsB < neighborsA:
                        closestPoint = [x,y]

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




pos = [0,1]
board = [
            "-b---",
            "-----",
            "-----",
            "-d---",
            "-----",
        ]

next_move(pos[0], pos[1], board)
