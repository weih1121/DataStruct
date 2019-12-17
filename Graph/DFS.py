from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def DFS(self, vertex):
        if not vertex in self.graph:
            print('vertex {} not exists in graph'.format(vertex))
            return 
        
        visited = [0] * len(self.graph)
        stack = [vertex]
        while stack:
            stack_top = stack[-1]
            print(stack_top)
            visited[stack_top] = 1
            stack_top.push(self.graph[stack_top])