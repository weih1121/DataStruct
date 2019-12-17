class AdjNode:
    '''
        邻接节点
    '''
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    '''
        图：数组 + 链接链表
    '''
    def __init__(self, vertices):
        self.V = vertices               # 图的节点个数 
        self.graph = [None] * self.V    # 每个节点对应的邻接链表
    
    def add_edge(self, src, dest):
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):
        for vertex in range(self.V):
            print('Node {} 邻接点: '.format(vertex))
            tmp = self.graph[vertex]
            print('Header', end='')
            while tmp:
                print('->{}'.format(tmp.vertex), end='')
                tmp = tmp.next
            print()

if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()
