import sys
def TSP(u,cost,minCost):
  if False not in visited:
    if adj[u][0]:
      cost += adj[u][0]
      minCost[0] = min(cost,minCost[0])
    return

  for v in range(V):
    if not visited[v] and adj[u][v]:
      visited[v] = True
      TSP(v, cost+adj[u][v], minCost)
      visited[v] = False

V,E = map(int,input("Enter no. of vertices and edges : ").split())
adj = [[0]*V for _ in range(V)]
visited = [False]*V
for i in range(E):
  u,v,wt = map(int,input(f"Edge-{i+1} : ").split())
  adj[u][v] = adj[v][u] = wt

minCost = [sys.maxsize]
TSP(0,0,minCost)
print("minCost : ",minCost)
