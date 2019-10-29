import copy 

board = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]

def solve(board):

    try:
        fillObv(board)
    except:
        return False

    if complete(board):
        return True
        
    i, j = 0, 0
    for x in range(9):
        for y in range(9):
            if board[y][x] == ".":
                i, j = x, y

    pos = getPos(board, i, j)

    for p in pos:
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
                    raise RuntimeError("No moves!")
                if len(pos) == 1:
                    board[y][x] = pos[0]
                    changed = True
            
        if changed == False:
            return
                
def complete(board):
    for y in range(9):
        for x in range(9):
            if board[y][x] == '.':
                return False
    return True
            
def getPos(board, x, y):
    if board[y][x] != '.':
        return False

    pos = { str(i) for i in range(1, 10) }
        
    for p in board[y]:
        pos -= { p }
        
    for i in range(9):
        pos -= { board[i][x] }
        
    sx = (x // 3) * 3
    sy = (y // 3) * 3
        
    for i in range(sy, sy + 3):
        for j in range(sx, sx + 3):
            pos -= { board[i][j] }

    return list(pos)

def printBoard(board):
    for x in range(9):
        for y in range(9):
            print(board[y][x], end="")
        print()
        
def main():

    solve(board)    
    printBoard(board)

main()