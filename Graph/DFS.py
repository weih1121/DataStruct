class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {}
        for i in range(self.vertices):
            self.graph[i] = []
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def DFS_util(self, vertex, visited):
        print(vertex)
        visited[vertex] = 1
        for i in self.graph[vertex]:
            if not visited[i]:
                self.DFS_util(i, visited)


    def DFS(self, vertex):
        if not vertex in self.graph:
            print('vertex {} not exists in graph'.format(vertex))
            return 
        
        visited = [0] * len(self.graph)
        self.DFS_util(vertex, visited)

        for i in self.graph:
            if i != vertex:
                if not visited[i]:
                    self.DFS_util(i, visited)

    
    def DFS_nonrecur_util(self, vertex, visited):
        if not vertex in self.graph:
            print('vertex {} not exists in graph'.format(vertex))
            return 
        
        stack = [vertex]
        while stack:
            stack_top = stack.pop()
            if not visited[stack_top]:
                print(stack_top)
                visited[stack_top] = 1
            
            for ver in self.graph[stack_top]:
                if not visited[ver]:
                    stack.append(ver)
    
    def DFS_nonrecur(self, vertex):
        visited = [0] * self.vertices
        self.DFS_nonrecur_util(vertex, visited)

        for i in self.graph:
            if not visited[i] and vertex != i:
                self.DFS_nonrecur_util(i, visited)


if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(1, 0)  
    g.add_edge(2, 1)  
    g.add_edge(3, 4)  
    g.add_edge(4, 0)
    
    print("Following is Depth First Traversal(non recur)")  
    g.DFS_nonrecur(0) 
    print("Following is Depth First Traversal")  
    g.DFS(0)