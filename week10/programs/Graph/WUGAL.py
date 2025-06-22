import heapq

class WeightedUndirectedGraph:
    def __init__(self, edges=None):
        self.adj_list = {}  # Adjacency list as {node: {neighbor: weight}}
        if edges:
            for start, end, weight in edges:
                self.add_edge(start, end, weight)

    def add_edge(self, u, v, weight):
        """Adds an undirected edge with weight."""
        if u not in self.adj_list:
            self.adj_list[u] = {}
        if v not in self.adj_list:
            self.adj_list[v] = {}
        self.adj_list[u][v] = weight  # Edge u -> v
        self.adj_list[v][u] = weight  # Edge v -> u (undirected)

    def add_vertex(self, vertex):
        """Adds a new vertex if not already present."""
        if vertex not in self.adj_list:
            self.adj_list[vertex] = {}
            print(f"New vertex added: {vertex}")
        else:
            print(f"Vertex {vertex} already exists")

    def remove_vertex(self, vertex):
        """Removes a vertex and all its edges."""
        if vertex in self.adj_list:
            del self.adj_list[vertex]  # Remove the vertex itself
            for node in self.adj_list:
                if vertex in self.adj_list[node]:  # Remove edges from other nodes
                    del self.adj_list[node][vertex]
            print(f"Vertex removed: {vertex}")
        else:
            print(f"Vertex {vertex} does not exist")

    def remove_edge(self, u, v):
        """Removes an undirected edge."""
        if u in self.adj_list and v in self.adj_list[u]:
            del self.adj_list[u][v]
        if v in self.adj_list and u in self.adj_list[v]:
            del self.adj_list[v][u]
        print(f"Edge removed: {u} <-> {v}")

    def longest_path(self, start, end, path=None, weight=0):
        """Finds the longest path using DFS."""
        if start not in self.adj_list:
            return [], 0
        if path is None:
            path = []
        path = path + [start]

        if start == end:
            return path, weight

        longest, max_weight = [], 0
        for neighbor, w in self.adj_list.get(start, {}).items():
            if neighbor not in path:
                new_path, new_weight = self.longest_path(neighbor, end, path, weight + w)
                if new_weight > max_weight:
                    longest, max_weight = new_path, new_weight
        return longest, max_weight

    def shortest_path(self, start, end):
        """Finds the shortest path using Dijkstra's Algorithm."""
        if start not in self.adj_list or end not in self.adj_list:
            return None, float('inf')

        min_heap = [(0, start, [])]  # (current_weight, node, path)
        visited = set()

        while min_heap:
            curr_weight, node, path = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            path = path + [node]

            if node == end:
                return path, curr_weight

            for neighbor, weight in self.adj_list.get(node, {}).items():
                if neighbor not in visited:
                    heapq.heappush(min_heap, (curr_weight + weight, neighbor, path))

        return None, float('inf')  # No path found

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
                queue.extend(self.adj_list.get(curr, {}).keys())
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
                stack.extend(self.adj_list.get(curr, {}).keys())  
        print()
        return visited


# Example Usage:
edges = [(0, 1, 4), (0, 2, 2), (1, 3, 5), (2, 4, 3), (3, 4, 1), (4, 5, 6)]
graph = WeightedUndirectedGraph(edges)

print("Graph Representation:", graph.adj_list)
graph.add_edge(5, 6, 2)
graph.add_vertex(7)
graph.remove_edge(0, 2)
graph.remove_vertex(3)

print("\nLongest Path from 0 to 5:", graph.longest_path(0, 5))
print("Shortest Path from 0 to 5:", graph.shortest_path(0, 5))

graph.bfs(0)
graph.dfs(0)
