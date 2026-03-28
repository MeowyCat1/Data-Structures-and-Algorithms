class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.list = []
        for i in range(num_nodes):
            self.list.append([])

    def add_edge(self, node_a, node_b):
        self.list[node_a].append(node_b)
        self.list[node_b].append(node_a)

    def bfs(self, start_num):
        self.visited = []
        for i in range(self.num_nodes):
            self.visited.append(False)
        result = []
        queue = []
        queue.append(start_num)
        self.visited[start_num] = True
        while len(queue) > 0:
            result.append(queue[0])
            temp = queue[0]
            queue.pop(0)
            for item in self.list[temp]:
                if self.visited[item] == False:
                    queue.append(item)
                    self.visited[item] = True
            

        return result

    def dfs(self):
        pass

        
mygraph = Graph(5)
mygraph.add_edge(0,2)
mygraph.add_edge(2,1)
mygraph.add_edge(1,4)
mygraph.add_edge(0,4)
mygraph.add_edge(4,3)
mygraph.add_edge(2,3)

print(mygraph.list)

print(mygraph.bfs(2))