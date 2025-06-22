class UnweightedDirectedGraphMatrix:
    def __init__(self, size=5):
        """Initializes an adjacency matrix with a given size."""
        self.size = size
        self.matrix = [[0] * size for _ in range(size)]  # Create an NxN matrix

    def add_vertex(self):
        """Adds a new vertex by expanding the adjacency matrix."""
        self.size += 1
        for row in self.matrix:
            row.append(0)  # Add a new column
        self.matrix.append([0] * self.size)  # Add a new row

    def add_edge(self, u, v):
        """Adds a directed edge u → v."""
        if u >= self.size or v >= self.size:
            print(f"Error: Node {max(u, v)} does not exist.")
            return
        self.matrix[u][v] = 1  # Set edge in the adjacency matrix

    def remove_edge(self, u, v):
        """Removes the directed edge u → v."""
        if u >= self.size or v >= self.size:
            print(f"Error: Node {max(u, v)} does not exist.")
            return
        self.matrix[u][v] = 0  # Remove the edge

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
        """Finds the shortest path using BFS."""
        if start >= self.size or end >= self.size:
            return None
        
        from collections import deque
        queue = deque([(start, [start])])  # (node, path)
        visited = set()

        while queue:
            node, path = queue.popleft()
            if node == end:
                return path
            
            for neighbor, exists in enumerate(self.matrix[node]):
                if exists and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return None  # No path found

    def longest_path(self, start, end, path=None, visited=None):
        """Finds the longest path using DFS."""
        if start >= self.size or end >= self.size:
            return []

        if path is None:
            path = []
        if visited is None:
            visited = set()

        path = path + [start]
        visited.add(start)

        if start == end:
            return path

        longest = []
        for neighbor, exists in enumerate(self.matrix[start]):
            if exists and neighbor not in visited:
                new_path = self.longest_path(neighbor, end, path, visited)
                if len(new_path) > len(longest):
                    longest = new_path

        visited.remove(start)
        return longest

    def bfs(self, start):
        """Performs Breadth-First Search (BFS) traversal."""
        visited = set()
        queue = [start]

        print("\nBFS Traversal:")
        while queue:
            curr = queue.pop(0)
            if curr not in visited:
                print(curr, end=" ")
                visited.add(curr)
                for neighbor, exists in enumerate(self.matrix[curr]):
                    if exists and neighbor not in visited:
                        queue.append(neighbor)
        print()

    def dfs(self, start, visited=None):
        """Performs Depth-First Search (DFS) traversal."""
        if visited is None:
            visited = set()

        if start in visited:
            return
        visited.add(start)

        print(start, end=" ")
        for neighbor, exists in enumerate(self.matrix[start]):
            if exists and neighbor not in visited:
                self.dfs(neighbor, visited)

    def display(self):
        """Displays the adjacency matrix."""
        print("\nAdjacency Matrix:")
        for row in self.matrix:
            print(row)


# Example Usage:
graph = UnweightedDirectedGraphMatrix(6)  # Create a graph with 6 vertices

edges = [(0, 1), (0, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
for u, v in edges:
    graph.add_edge(u, v)

graph.display()

graph.add_vertex()
graph.add_edge(5, 6)
graph.remove_edge(0, 2)
graph.remove_vertex(3)

print("\nShortest Path from 0 to 5:", graph.shortest_path(0, 5))
print("Longest Path from 0 to 5:", graph.longest_path(0, 5))

graph.bfs(0)
print("\nDFS Traversal:")
graph.dfs(0)
print()
