import heapq

def dijkstra(adj_list, start):
    vertices = len(adj_list)
    distances = [float('inf')] * vertices
    distances[start] = 0
    min_heap = [(0, start)]
    while min_heap:
        current_distance, current_vertex = heapq.heappop(min_heap)

        if current_distance > distances[current_vertex]:
            continue

        for n, d in adj_list[current_vertex]:
            dist = current_distance + d
            if dist < distances[n]:
                distances[n] = dist
                heapq.heappush(min_heap, (dist, n))

    return distances


vertices = int(input("Enter the number of vertices: "))
adj_list = [[] for _ in range(vertices)]

while True:
    edge_input = input("Enter an edge (u v w) or 'done' to finish: ")
    if edge_input.lower() == 'done':
        break
    u, v, w = map(int, edge_input.split())
    adj_list[u].append((v, w))
    adj_list[v].append((u, w))

start_node = int(input("Enter the start node: "))

distances = dijkstra(adj_list, start_node)
print(f"\nShortest distances from node {start_node}")
for i in range(len(distances)):
    print(f"Distance to node {i}: {distances[i]}")
