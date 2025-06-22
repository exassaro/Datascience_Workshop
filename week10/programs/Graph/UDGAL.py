#UnWeighted Directed Graph usinng an adjancey List
class Digraph:
    def __init__(self, edges=None):
        self.dict={}
        if edges:
            for start,end in edges:
                self.add_edge(start,end)
    
    def add_edge(self,start,end):
        if start not in self.dict:
            self.dict[start]=[]
        self.dict[start].append(end)
        
    def add_edges(self,vertex,edges):
        if vertex not in self.dict:
            self.dict[vertex] = edges
        else:
            self.dict[vertex].extend(edges)
            
    def add_vertex(self, vertex):
        if vertex not in self.dict:
            self.dict[vertex] = []
            print("New vertex added:", vertex)
        else:
            print("Vertex already exists:", vertex)
            
    def remove_vertex(self, vertex):
        if vertex in self.dict:
            for key in list(self.dict):
                if vertex in self.dict[key]:
                    self.dict[key].remove(vertex)
            del self.dict[vertex]
            print("Vertex removed:", vertex)
        else:
            print("Vertex does not exist:", vertex)

    def remove_edge(self, vertex, edge):
        if vertex in self.dict and edge in self.dict[vertex]:
            self.dict[vertex].remove(edge)
            print(f"Edge removed: {vertex} -> {edge}")
        else:
            print("Edge does not exist")
            
    def longest_path(self, start, end, path=None):
        if start not in self.dict:
            return []
        if path is None:
            path = []
        path = path + [start]

        if start == end:
            return path
        
        longest = []
        for neighbor in self.dict.get(start, []):
            if neighbor not in path:
                new_path = self.longest_path(neighbor, end, path)
                if len(new_path) > len(longest):
                    longest = new_path
        return longest

    def shortest_path(self, start, end, path=None):
        if start not in self.dict:
            return None
        if path is None:
            path = []
        path = path + [start]

        if start == end:
            return path

        shortest = None
        for neighbor in self.dict.get(start, []):
            if neighbor not in path:
                new_path = self.shortest_path(neighbor, end, path)
                if new_path:
                    if shortest is None or len(new_path) < len(shortest):
                        shortest = new_path
        return shortest
    
    def bfs(self, node):
        visited = set()
        queue = [node]

        print("\nBFS Traversal:")
        while queue:
            curr = queue.pop(0)
            if curr not in visited:
                print(curr, end=" ")
                visited.add(curr)
                queue.extend(self.dict.get(curr, []))
        print()
        return visited

    def dfs(self, node):
        visited = set()
        stack = [node]

        print("\nDFS Traversal:")
        while stack:
            curr = stack.pop()
            if curr not in visited:
                print(curr, end=" ")
                visited.add(curr)
                stack.extend(self.dict.get(curr, []))  
        print()
        return visited


edges = [(0, 1), (0, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
graph = Digraph(edges)

print("Graph Representation:", graph.dict)
graph.add_edge(5, 6)
graph.add_vertex(7)


print("\nLongest Path from 0 to 5:", graph.longest_path(0, 5))
print("Shortest Path from 0 to 5:", graph.shortest_path(0, 5))


graph.bfs(0)
graph.dfs(0)

graph.remove_edge(0, 2)
graph.remove_vertex(3)
