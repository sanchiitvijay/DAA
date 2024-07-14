import heapq

def create_graph(vertices):
    return [[] for _ in range(vertices)]

def add_edge(adj_list, u, v, w):
    adj_list[u].append((v, w))
    adj_list[v].append((u, w))

def display_graph(adj_list):
    for i in range(len(adj_list)):
        print(f"Vertex {i}:", end="")
        for (j, weight) in adj_list[i]:
            print(f" -> {j} (weight {weight})", end="")
        print()

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
            distance = current_distance + d
            if distance < distances[n]:
                distances[n] = distance
                heapq.heappush(min_heap, (distance, n))

    return distances

vertices = int(input("Enter the number of vertices: "))

adj_list = create_graph(vertices)

while True:
    edge_input = input("Enter an edge (u v w) or 'done' to finish: ")
    if edge_input.lower() == 'done':
        break
    u, v, w = map(int, edge_input.split())
    add_edge(adj_list, u, v, w)

print("Graph:")
display_graph(adj_list)

start_node = int(input("Enter the start node: "))

distances = dijkstra(adj_list, start_node)
print(f"\nShortest distances from node {start_node}")
for i in range(len(distances)):
    print(f"Distance to node {i}: {distances[i]}")
