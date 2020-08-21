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
    g.addEdge(u,v)
visited = [False]*(V+1)
def dfs(g,node):
    x = node.data
    visited[x] = True
    for x in node.connections:
       if not visited[x]:
           dfs(g,g.vertices[x]) 
ans= 0
for x in range(1,V+1):
    if not visited[x]:
        ans+=1
        dfs(g,g.vertices[x])
print(ans)