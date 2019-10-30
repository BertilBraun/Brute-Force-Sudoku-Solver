import copy

board = [[".",".",".","2",".",".",".","6","3"],["3",".",".",".",".","5","4",".","1"],[".",".","1",".",".","3","9","8","."],[".",".",".",".",".",".",".","9","."],[".",".",".","5","3","8",".",".","."],[".","3",".",".",".",".",".",".","."],[".","2","6","3",".",".","5",".","."],["5",".","3","7",".",".",".",".","8"],["4","7",".",".",".","1",".",".","."]]

def main():
    solve()
    printBoard()
    
       
def solve():    
    global board

    if fillAllObvious() == False:
        return False
    
    if isComplete():
        return True
    
    for rowIdx in range(9):
        for colIdx in range(9):
            if board[rowIdx][colIdx] == ".":
                for value in getPossibilities(rowIdx, colIdx):
                    snapshot = copy.deepcopy(board)

                    board[rowIdx][colIdx] = value
                    if solve() == True:
                        return True
                    else:
                        board = copy.deepcopy(snapshot)
                        
                return False

def fillAllObvious():
    while True:
        changed = False
        for i in range(0,9):
            for j in range(0,9):
            
                possibilities = getPossibilities(i,j)
                
                if possibilities == False:
                    continue
                if len(possibilities) == 0:
                    return False
                if len(possibilities) == 1:
                    board[i][j] = possibilities[0]
                    changed = True
                    
        if changed == False:
            return True
                
def getPossibilities(i,j):
    if board[i][j] != ".":
        return False
          
    iStart = (i // 3) * 3
    jStart = (j // 3) * 3
    
    possibilities = {str(n) for n in range(1,10)}
    
    possibilities -= { val for val in board[i] }
    possibilities -= { board[idx][j] for idx in range(0,9) }      
    possibilities -= { board[y][x] for x in range(jStart, jStart + 3) for y in range(iStart, iStart + 3) }
    
    return list(possibilities)

def printBoard():
    for row in board:
        for col in row:
            print(col, end="")
        print()
        
def isComplete():
    for row in board:
        for col in row:
            if (col == "."):
                return False                
    return True
    
main()
