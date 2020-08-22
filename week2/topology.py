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
incoming = [0]*(V+1)
outgoing= [0]*(V+1)
g.addVertices([x for x in range(1,V+1)])
for x in range(e):
    u,v = [int(i) for i in input().split()]
    g.addEdge(u,v,'d')
    outgoing[u]+=1
    incoming[v]+=1  
ans = []    
visited = [False]*(V+1)           
def topology(g,node):
    visited[node.data] = True
    ans.append(node.data)
    # print(node.data)
    for y in node.connections:
        incoming[y]-=1
        if incoming[y]==0 and not visited[y]:
           topology(g,g.vertices[y])
for x in range(1,V+1):
    if incoming[x]==0 and not visited[x]:
        topology(g,g.vertices[x])
for i in range(V-1):
    print("{} ".format(ans[i]),end="")
print(ans[V-1])