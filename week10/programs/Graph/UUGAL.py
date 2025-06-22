class Graph:
    def __init__(self, edges=None):
        self.adj_list = {}  # Dictionary to store adjacency list
        if edges:
            for start, end in edges:
                self.add_edge(start, end)

    def add_edge(self, start, end):
        """Adds an undirected edge between start and end."""
        if start not in self.adj_list:
            self.adj_list[start] = []
        if end not in self.adj_list:
            self.adj_list[end] = []
        self.adj_list[start].append(end)
        self.adj_list[end].append(start)  # Add reverse edge

    def add_vertex(self, vertex):
        """Adds a new vertex if not already present."""
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            print(f"New vertex added: {vertex}")
        else:
            print(f"Vertex {vertex} already exists")

    def remove_vertex(self, vertex):
        """Removes a vertex and all its connections."""
        if vertex in self.adj_list:
            for neighbor in self.adj_list[vertex]:  # Remove vertex from neighbors
                self.adj_list[neighbor].remove(vertex)
            del self.adj_list[vertex]
            print(f"Vertex removed: {vertex}")
        else:
            print(f"Vertex {vertex} does not exist")

    def remove_edge(self, start, end):
        """Removes an edge between start and end."""
        if start in self.adj_list and end in self.adj_list[start]:
            self.adj_list[start].remove(end)
        if end in self.adj_list and start in self.adj_list[end]:
            self.adj_list[end].remove(start)
        print(f"Edge removed: {start} - {end}")

    def longest_path(self, start, end, path=None):
        """Finds the longest path from start to end (Recursive DFS)."""
        if start not in self.adj_list:
            return []
        if path is None:
            path = []
        path = path + [start]

        if start == end:
            return path

        longest = []
        for neighbor in self.adj_list[start]:
            if neighbor not in path:
                new_path = self.longest_path(neighbor, end, path)
                if len(new_path) > len(longest):
                    longest = new_path
        return longest

    def shortest_path(self, start, end):
        """Finds the shortest path using BFS."""
        if start not in self.adj_list or end not in self.adj_list:
            return None

        queue = [(start, [start])]
        visited = set()

        while queue:
            curr, path = queue.pop(0)
            if curr == end:
                return path
            if curr not in visited:
                visited.add(curr)
                for neighbor in self.adj_list.get(curr, []):
                    queue.append((neighbor, path + [neighbor]))

        return None  # No path found

    def bfs(self, start):
        """Breadth-First Search (BFS) Traversal."""
        visited = set()
        queue = [start]

        print("\nBFS Traversal:")
        while queue:
            curr = queue.pop(0)
            if curr not in visited:
                print(curr, end=" ")
                visited.add(curr)
                queue.extend(self.adj_list.get(curr, []))
        print()
        return visited

    def dfs(self, start):
        """Depth-First Search (DFS) Traversal."""
        visited = set()
        stack = [start]

        print("\nDFS Traversal:")
        while stack:
            curr = stack.pop()
            if curr not in visited:
                print(curr, end=" ")
                visited.add(curr)
                stack.extend(self.adj_list.get(curr, []))  
        print()
        return visited


# Example Usage:
edges = [(0, 1), (0, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
graph = Graph(edges)

print("Graph Representation:", graph.adj_list)
graph.add_edge(5, 6)
graph.add_vertex(7)
graph.remove_edge(0, 2)
graph.remove_vertex(3)

print("\nLongest Path from 0 to 5:", graph.longest_path(0, 5))
print("Shortest Path from 0 to 5:", graph.shortest_path(0, 5))

graph.bfs(0)
graph.dfs(0)
