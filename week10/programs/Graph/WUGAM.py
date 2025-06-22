import heapq

class WeightedUndirectedGraphMatrix:
    def __init__(self, size=5):
        """Initializes an adjacency matrix for a weighted undirected graph."""
        self.size = size
        self.matrix = [[float('inf')] * size for _ in range(size)]  # Create NxN matrix
        for i in range(size):
            self.matrix[i][i] = 0  # Distance to itself is 0

    def add_vertex(self):
        """Adds a new vertex by expanding the adjacency matrix."""
        self.size += 1
        for row in self.matrix:
            row.append(float('inf'))  # Add a new column
        self.matrix.append([float('inf')] * self.size)  # Add a new row
        self.matrix[-1][-1] = 0  # Distance to itself is 0

    def add_edge(self, u, v, weight):
        """Adds an undirected weighted edge (u ↔ v)."""
        if u >= self.size or v >= self.size:
            print(f"Error: Node {max(u, v)} does not exist.")
            return
        self.matrix[u][v] = weight  # u → v
        self.matrix[v][u] = weight  # v → u (undirected)

    def remove_edge(self, u, v):
        """Removes an undirected edge (u ↔ v)."""
        if u >= self.size or v >= self.size:
            print(f"Error: Node {max(u, v)} does not exist.")
            return
        self.matrix[u][v] = float('inf')  # Remove edge u → v
        self.matrix[v][u] = float('inf')  # Remove edge v → u (undirected)

    def remove_vertex(self, vertex):
        """Removes a vertex and updates the adjacency matrix."""
        if vertex >= self.size:
            print(f"Error: Vertex {vertex} does not exist.")
            return

        # Remove the row
        del self.matrix[vertex]

        # Remove the column
        for row in self.matrix:
            del row[vertex]

        self.size -= 1

    def shortest_path(self, start, end):
        """Finds the shortest weighted path using Dijkstra's Algorithm."""
        if start >= self.size or end >= self.size:
            return None

        distances = [float('inf')] * self.size
        distances[start] = 0
        pq = [(0, start)]  # (distance, node)
        previous = {start: None}

        while pq:
            curr_dist, node = heapq.heappop(pq)

            if node == end:
                path = []
                while node is not None:
                    path.insert(0, node)
                    node = previous[node]
                return path

            for neighbor in range(self.size):
                weight = self.matrix[node][neighbor]
                if weight != float('inf'):
                    new_dist = curr_dist + weight
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heapq.heappush(pq, (new_dist, neighbor))
                        previous[neighbor] = node

        return None  # No path found

    def display(self):
        """Displays the adjacency matrix."""
        print("\nAdjacency Matrix:")
        for row in self.matrix:
            print(row)


# Example Usage:
graph = WeightedUndirectedGraphMatrix(6)  # Create a graph with 6 vertices

edges = [(0, 1, 2), (0, 2, 5), (1, 3, 1), (2, 4, 3), (3, 4, 4), (4, 5, 2)]
for u, v, w in edges:
    graph.add_edge(u, v, w)

graph.display()

graph.add_vertex()
graph.add_edge(5, 6, 7)
graph.remove_edge(0, 2)
graph.remove_vertex(3)

print("\nShortest Path from 0 to 5:", graph.shortest_path(0, 5))
