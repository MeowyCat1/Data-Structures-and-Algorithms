class ConnectedGraph:
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

    def dfs(self, startnum):
        self.visited = [False] * self.num_nodes
        result = []
        self.dfsutil(startnum, self.visited, result)
        return result
    
    def dfsutil(self, temp, node, visited):
        visited[node] = True
        temp.append(node)
        for i in self.list[node]:
            if not self.visited[i]:
                temp = self.dfsutil(temp, i, visited)

        return temp

    def connected_components(self):
        self.visited = [False] * self.num_nodes
        cc = []
        for node in range(len(self.list)):
            if not self.visited[node]:
                temp = []
                t = self.dfsutil(temp, node, self.visited)
                cc.append(t)

        return cc
    
myconnectedgraph = ConnectedGraph(5)
myconnectedgraph.add_edge(0, 1)
myconnectedgraph.add_edge(0, 2)
myconnectedgraph.add_edge(3, 4)

print(myconnectedgraph.connected_components())