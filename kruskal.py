class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((w, u, v))

    def find(self, i, parent):
        if parent[i] == i:
            return i
        return self.find(parent[i], parent)

    def union(self, u, v, parent, rank):
        root_x = self.find(u, parent)
        root_y = self.find(v, parent)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_y] < rank[root_x]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal_mst(self):
        mst = []
        parent = []
        rank = []

        # Sort edges by weight
        self.edges.sort()

        # Initialize parent and rank
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)

        i = 0
        e = 0

        while e < self.vertices - 1:
            weight, u, v = self.edges[i]
            i += 1

            x = self.find(u, parent)
            y = self.find(v, parent)

            if x != y:
                mst.append((u, v, weight))
                e += 1
                self.union(u, v, parent, rank)

        return mst

vertices = int(input("Enter the number of vertices: "))

g = Graph(vertices)

while True:
    edge_input = input("Enter an edge (u v w) or 'done' to finish: ")
    if edge_input.lower() == 'done':
        break
    u, v, w = map(int, edge_input.split())
    g.add_edge(u, v, w)

mst = g.kruskal_mst()
print("\nMinimum Spanning Tree:")
for edge in mst:
    print(f"{edge[0]} - {edge[1]}: {edge[2]}")
