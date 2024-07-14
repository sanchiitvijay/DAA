def isSafe(arr, row, col, n):
   
    for i in range(col, n):
        if arr[row][i]:
            return False
  
    i, j = row, col
    while i >= 0 and j < n:
        if arr[i][j]:
            return False
        i -= 1
        j += 1

    i, j = row, col
    while i < n and j < n:
        if arr[i][j]:
            return False
        i += 1
        j += 1

    return True

def nQueens(arr, n, column):
    if column == -1:
        return True
    
    for i in range(n):
        if arr[i][column] == 0:
            if isSafe(arr, i, column, n):
                arr[i][column] = 1
                if nQueens(arr, n, column - 1):
                    return True
                arr[i][column] = 0  
    
    return False

n = 4 
arr = [[0] * n for _ in range(n)]

if nQueens(arr, n, n -1):
    for row in arr:
        print(row)
else:
    print("No solution found")
