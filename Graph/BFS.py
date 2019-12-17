from collections import defaultdict
import queue

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def BFS(self, vertex):
        if not vertex in self.graph:
            print('Trere is no {} in graph'.format(vertex))
            return

        visited = [False] * len(self.graph)
        q = queue.Queue()
        q.put(vertex)

        while not q.empty():
            vertex_pop = q.get()
            print(vertex_pop)
            visited[vertex_pop] = True
            for item in self.graph[vertex_pop]:
                if not visited[item]:
                    q.put(item)
    
        

    
if __name__ == "__main__":
    g = Graph() 
    g.add_edge(0, 1) 
    g.add_edge(0, 2) 
    g.add_edge(1, 2) 
    g.add_edge(2, 0) 
    g.add_edge(2, 3) 
    g.add_edge(3, 3) 
    
    print ("Following is Breadth First Traversal"
                    " (starting from vertex 2)") 
    g.BFS(2) 

