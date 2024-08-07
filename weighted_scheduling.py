def WeightedIntervalScheduling():
  intervals.sort(key = lambda x: x[1])
  n = len(intervals)

  for i in range(1,n):
    j = i-1
    while intervals[j][1] >= intervals[i][0]:
      j -= 1
    P.append(j)

  M = [0]*n
  for i in range(1,n):
    M[i] = max(intervals[i][2]+M[P[i]], M[i-1])

  return M


# if asked to print all the intervals included in the solution
def FindSolution(M):
  included = []
  j = len(M)-1
  while j:
    if intervals[j][2] + M[P[j]] > M[j-1]:
      included.append(intervals[j])
      j = P[j]
    else:
      j -= 1
  return included


intervals = [(-1,-1,-1)]
print("Enter intervals :")
while True:
  interval = input()
  if interval:
    s,f,val = map(int,interval.split())
    intervals.append((s,f,val))
  else:
    break

P = [0]
M = WeightedIntervalScheduling()
print("Maximum value obtainable is :",M[-1])

included = FindSolution(M)
print("\nThe intervals included are : ")
print("\n| Start | Finish | Value |")
for s,f,val in included:
  print("|%7d|%8d|%7d|"%(s,f,val))

# 1 2 100
# 2 5 200
# 3 6 300
# 4 8 400
# 5 9 500
# 6 10 100