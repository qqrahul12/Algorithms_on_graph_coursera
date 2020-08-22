import sys
class graphNode():
    def __init__(self,data):
        self.data = data
        self.connections = []
class graph():
    def __init__(self):
        self.vertices = {}
    def addVertices(self,v):
        for x in v:
            node = graphNode(x)
            self.vertices[x] = node
    def addEdge(self,v1,v2,type='u'):
        self.vertices[v1].connections.append(v2)
        if type=='u':
            self.vertices[v2].connections.append(v1)
    def __str__(self):
        return "Vertices = {} ".format(len(self.vertices))
V,e = [int(i) for i in input().split()]
g = graph()
g.addVertices([x for x in range(1,V+1)])
for x in range(e):
    u,v = [int(i) for i in input().split()]
    g.addEdge(u,v,'d')
visited = [False]*(V+1)
stack = [False]*(V+1)
def isCycle(g,node):
    x = node.data
    visited[x] = True
    stack[x] = True
    for y in node.connections:
        if not visited[y]:
           if isCycle(g,g.vertices[y]) == True:
               return True
        elif stack[y]:
            # print(y)
            return True
    stack[x] = False
    return False
ans = False
for x in range(1,V+1):
    if not visited[x]:
        if isCycle(g,g.vertices[x]) == True:
            # print(x)
            ans = True
if ans==True:
    print("{}".format(1))
else:
    print("{}".format(0))
