#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    m = []
    p = []
    print(enumerate(grid))
    for y, row in enumerate(grid):
        print(y, row)
        if 'm' in row:
            m = [row.index('m'), y]
        if 'p' in row:
            p = [row.index('p'), y] 
   
    print(m,p)
    while m[0] != p[0]:
        if m[0] < p[0]:
            print('RIGHT')
            m[0] += 1
        elif m[0] > p[0]:
            print('LEFT')
            m[0] -= 1
        

    while m[1]!= p[1]:
        if m[1] < p[1]:
            print('DOWN')
            m[1] += 1
        elif m[1] > p[1]:
            print('UP')
            m[1] -= 1
        



grid = [['-','p','-'],
        ['-','m','-'],
        ['-','-','-']] 

displayPathtoPrincess(3,grid)