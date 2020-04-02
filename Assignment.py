from collections import defaultdict


class StronglyConnectedComponent:
    t = 1
    num = 1

    # creating the Graph
    def __init__(self, v):
        self.vertices = v
        self.node = defaultdict(list)

    # adding the edges and nodes to the graph
    def addEdge(self, u, v):
        self.node[u].append(v)
        print("Edge Added: Source", u, "-->", "Target", v)

    def dfs(self, pre, post):
        # initializing the empty stack
        stack = []
        # boolean check list for visited nodes
        visited = [False] * self.vertices
        # first dfs traversal
        for i in range(self.vertices):
            if not visited[i]:
                self.visitedNode(i, pre, post, stack, visited)

        # Creating the transpose graph for the second DFS traversal
        print("Edges of the transpose graph:")
        tGrapgh = self.transposeGraph()
        # making all the nodes unvisited for the second graph
        visited = [False] * self.vertices

        while stack:
            i = stack.pop()
            if not visited[i]:
                print(self.num, "number SCC: ", end='')
                self.num = self.num + 1
                tGrapgh.dfsInTraversalGraph(i, visited)
                print("")
        print("Total number of Strongly Connected Component in the graph:", (self.num - 1))

    # For the first dfs traversal
    def visitedNode(self, v, pre, post, stack, visited):
        # adding starting time
        pre[v] = self.t
        # updating the timer
        self.t = self.t + 1
        visited[v] = True
        for i in self.node[v]:
            if not visited[i]:
                # recursive function for DFS
                self.visitedNode(i, pre, post, stack, visited)
        # adding the finishing time
        post[v] = self.t
        # updating the timer
        self.t = self.t + 1
        print("Adding node", v, "to stack:", "Start time=", pre[v], "Finishing time=", post[v])
        # adding the completed node to the stack
        stack = stack.append(v)

    def transposeGraph(self):
        newGraph = StronglyConnectedComponent(self.vertices)
        for i in self.node:
            for j in self.node[i]:
                newGraph.addEdge(j, i)
        return newGraph

    def dfsInTraversalGraph(self, v, visited):
        # Mark the current node as visited and print it
        visited[v] = True
        print(v, "", end='')
        # DFS in the transpose graph
        for i in self.node[v]:
            if not visited[i]:
                self.dfsInTraversalGraph(i, visited)


ver = int(input("Please give the number of vertices: "))
graph = StronglyConnectedComponent(ver)
edg = int(input("Please give the number of edges: "))
for i in range(ver):
    source = int(input("Please give the source node: "))
    target = int(input("Please give the target node: "))
    graph.addEdge(source, target)
    print("")
pre = [0] * (ver)
post = [0] * (ver)
print("")
graph.dfs(pre, post)
print("")
