def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

def isSafe(board, row, col):
    if ld[row - col + N - 1] != 1 and rd[row + col] != 1 and cl[row] != 1:
        return True
    return False

def solveNQUtil(board, col):
    if col >= N:
        return True
    
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 1
            
            if solveNQUtil(board, col + 1):
                return True
            
            board[i][col] = 0
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 0
    
    return False

def solveNQ():
    board = [[0]*N for _ in range(N)]
    
    if not solveNQUtil(board, 0):
        print("Solution does not exist")
        return False
    
    printSolution(board)
    return True

N = int(input())

ld = [0] * (2 * N - 1)
rd = [0] * (2 * N - 1)
cl = [0] * N

solveNQ()
