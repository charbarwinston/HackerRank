#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    m = []
    p = []
    for y, row in enumerate(grid):
        if 'm' in row:
            m = [row.index('m'), y]
        if 'p' in row:
            p = [row.index('p'), y] 

    if m[0] < p[0]:
        return('RIGHT')
    elif m[0] > p[0]:
        return('LEFT')

    if m[1] < p[1]:
        return('DOWN')
    elif m[1] > p[1]:
        return('UP')
        



grid = [['-','-','-'],
        ['-','m','-'],
        ['p','-','-']] 

print(displayPathtoPrincess(3,grid))