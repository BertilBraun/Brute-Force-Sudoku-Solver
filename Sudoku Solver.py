import copy 

def solve(board):

    if fillObv(board) == False:
        return False

    if complete(board):
        return True
    
    i, j = 0, 0
    for y in range(9):
        for x in range(9):
            if board[y][x] == ".":
                i, j = x, y
                
    for p in getPos(board, i, j):
        old = copy.deepcopy(board)

        board[j][i] = p
        if solve(board) == True:
            return True
        else:
            board = copy.deepcopy(old)

    return False

def fillObv(board):
    while True:
        changed = False
            
        for x in range(9):
            for y in range(9):

                pos = getPos(board, x, y)

                if pos == False:
                    continue
                if len(pos) == 0:
                    return False
                if len(pos) == 1:
                    board[y][x] = pos[0]
                    changed = True
            
        if changed == False:
            return True
                
def complete(board):
    for col in board:
        for val in col:
            if val == '.':
                return False
    return True
            
def getPos(board, x, y):
    if board[y][x] != '.':
        return False

    sx = (x // 3) * 3
    sy = (y // 3) * 3
    
    pos = { str(i) for i in range(1, 10) }
    
    pos -= { p for p in board[y] }
    pos -= { col[x] for col in board }    
    pos -= { board[i][j] for j in range(sx, sx + 3) for i in range(sy, sy + 3) }
    
    return list(pos)

def printBoard(board):
    for y in range(9):
        for x in range(9):
            print(board[y][x], end="")
        print()
        
def main():

    sudoku = [
    [".",".",".","2",".",".",".","6","3"],
    ["3",".",".",".",".","5","4",".","1"],
    [".",".","1",".",".","3","9","8","."],
    [".",".",".",".",".",".",".","9","."],
    [".",".",".","5","3","8",".",".","."],
    [".","3",".",".",".",".",".",".","."],
    [".","2","6","3",".",".","5",".","."],
    ["5",".","3","7",".",".",".",".","8"],
    ["4","7",".",".",".","1",".",".","."]]
    
    print(solve(sudoku))
    printBoard(sudoku)

main()