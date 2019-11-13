#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    m = []
    p = []
    print(enumerate(grid))
    for y, row in enumerate(grid):
        if 'm' in row:
            m = [row.index('m') + 1, y ]
        if 'p' in row:
            p = [row.index('p') + 1, y]
    print(m,p)

grid = [['-','-','-'], #1
        ['-','m','-'], #2
        ['p','-','-']] #3

displayPathtoPrincess(3,grid)