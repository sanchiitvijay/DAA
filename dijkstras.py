import heapq,sys
def Dijkstra(s):
  dist = [sys.maxsize]*V
  dist[s] = 0
  pq = [(0,s)]
  while pq:
    d,u = heapq.heappop(pq)
    for v,w in adj[u]:
      if dist[v] > d+w:
        dist[v] = d+w
        heapq.heappush(pq,(dist[v],v))

  return dist

V,E = map(int,input("Enter the no. of vertices and edges : ").split())
adj = [[] for _ in range(V)]
print("\nEnter :")
for e in range(E):
  u,v,w = map(int,input(f"Edge-{e} : ").split())
  adj[u].append((v,w))
  adj[v].append((u,w))

src = int(input("Enter the source : "))
dist = Dijkstra(src)

for i in range(V):
  if dist[i] != sys.maxsize:
    print(f"Distance from {src} to {i} is {dist[i]}")
  else:
    print(f"No path from {src} to {i}")