def KnapSack():
  M = [[0]*(W+1) for _ in range(n+1)]
  for i in range(1,n+1):
    for w in range(1,W+1):
      if weights[i] > w:
        M[i][w] = M[i-1][w]
      else:
        M[i][w] = max(M[i-1][w], values[i]+M[i-1][w-weights[i]])
  return M


# Use this function in case external asked to show the items included in the knapsack
def FindSolution(M):
  i,w = n,W
  included = []
  while i:
    if weights[i]<=w and values[i]+M[i-1][w-weights[i]] > M[i-1][w]:
      included.append((weights[i],values[i]))
      w -= weights[i]
    i -= 1
  return included

n = int(input("Enter the no. of elements : "))
weights = [0]*(n+1)
values = [0]*(n+1)
for i in range(1,n+1):
  weights[i],values[i] = map(int,input(f"{i} : ").split())

W = int(input("Enter maximum capacity : "))
M = KnapSack()
print("Maximum value obtainable is : ",M[n][W])
print(FindSolution(M))

# Enter the no. of elements : 4
# 1 : 3 10
# 2 : 5 4
# 3 : 6 9
# 4 : 2 11
# Enter maximum capacity : 9