import tkinter as tk
grid = [['p','-','-'],
        ['-','m','-'],
        ['-','-','-']]
win = False
def gridMessage(message):
    global win
    global grid
    def getNextMove(grid):
        m = []
        p = []
        for y, row in enumerate(grid):
            if 'm' in row:
                m = [row.index('m'), y]
            if 'p' in row:
                print("found Peach")
                p = [row.index('p'), y] 

        if m[0] < p[0]:
            return(moveM('RIGHT', grid, m, p))
        elif m[0] > p[0]:
            return(moveM('LEFT', grid, m, p))
        elif m[1] < p[1]:
            return(moveM('DOWN', grid, m, p))
        elif m[1] > p[1]:
            return(moveM('UP', grid, m, p))

    def moveM(nextMove, grid, m, p):
        if nextMove == 'RIGHT':
            grid[m[0]][m[1]] = ''
            grid[m[0] + 1][m[1]] = 'm'
        elif nextMove == 'LEFT':
            grid[m[0]][m[1]] = '-'
            grid[m[0] - 1][m[1]] = 'm'
        elif nextMove == 'UP':
            grid[m[0]][m[1]] = '-'
            grid[m[0]][m[1] - 1] = 'm'
        elif nextMove == 'DOWN':
            grid[m[0]][m[1]] = '-'
            grid[m[0]][m[1] + 1] = 'm'
        checkWinCondition(grid)
        return(grid)

    def convertGridToText(grid):
        gridText = ""
        for x in grid:
            for i in x:
                gridText += i + " "
            gridText += '\n'

    def checkWinCondition(grid):
        global win
        for i in grid:
            for x in i:
                if x == 'p':
                    win = False
                    return 
        win = True
        return
        def getNextMove(grid):
            m = []
            p = []
            for y, row in enumerate(grid):
                if 'm' in row:
                    m = [row.index('m'), y]
                if 'p' in row:
                    print("found Peach")
                    p = [row.index('p'), y] 

            if m[0] < p[0]:
                return(moveM('RIGHT', grid, m, p))
            elif m[0] > p[0]:
                return(moveM('LEFT', grid, m, p))
            elif m[1] < p[1]:
                return(moveM('DOWN', grid, m, p))
            elif m[1] > p[1]:
                return(moveM('UP', grid, m, p))

    def moveM(nextMove, grid, m, p):
        if nextMove == 'RIGHT':
            grid[m[0]][m[1]] = ''
            grid[m[0] + 1][m[1]] = 'm'
        elif nextMove == 'LEFT':
            grid[m[0]][m[1]] = '-'
            grid[m[0] - 1][m[1]] = 'm'
        elif nextMove == 'UP':
            grid[m[0]][m[1]] = '-'
            grid[m[0]][m[1] - 1] = 'm'
        elif nextMove == 'DOWN':
            grid[m[0]][m[1]] = '-'
            grid[m[0]][m[1] + 1] = 'm'
        checkWinCondition(grid)
        return(grid)

    def convertGridToText(grid):
        gridText = ""
        for x in grid:
            for i in x:
                gridText += i + " "
            gridText += '\n'

    def checkWinCondition(grid):
        global win
        for i in grid:
            for x in i:
                if x == 'p':
                    win = False
                    return 
        win = True
        return
    def move(grid):
        message.config(text=str(convertGridToText(grid)))
        grid = getNextMove(grid)
        message.after(10000,move(grid))
    if not win:
        move(grid)

root = tk.Tk()
root.title("Grid")
message = tk.Message(root, fg="green", font="TkFixedFont")
message.pack()
gridMessage(message)

root.mainloop()