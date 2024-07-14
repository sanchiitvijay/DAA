def solveNQueens(n):
    def could_place(row, col):
        for i in range(row):
            if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                return False
        return True
    def place_queens(n, row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if could_place(row, col):
                board[row] = col
                place_queens(n, row + 1)
                board[row] = 0
    result = []
    board = [0] * n
    place_queens(n, 0)
    
    formatted_result = []
    for solution in result:
        formatted_board = []
        for col in solution:
            formatted_board.append("." * col + "q" + "." * (n - col - 1))
        formatted_result.append(formatted_board)
    
    return formatted_result
    
n = 4
solutions = solveNQueens(n)
for idx, solution in enumerate(solutions):
    print(f"Solution {idx + 1}:")
    for row in solution:
        print(row)
    print()
