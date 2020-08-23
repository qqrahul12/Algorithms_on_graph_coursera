import sys
sys.setrecursionlimit(200000)
from collections import defaultdict
class graph():
    def __init__(self,v):
        self.v = v
        self.cons = defaultdict(list)
    def addEdge(self,v1,v2,type='u'):
        self.cons[v1].append(v2)
        if type=='u':
            self.cons[v2].append(v1)
    def __str__(self):
        print("graph with {} vertices".format(self.v))
n,m = [int(i) for i in input().split()]
g = graph(n)
for j in range(m):
    x,y = [int(i) for i in input().split()]
    g.addEdge(x,y,'d')
visited = [False]*(n+1)
dfst = []
def dfs(g,x):
    visited[x] = True
    for y in g.cons[x]:
        if not visited[y]:
           visited[y] = True 
           dfs(g,y) 
    dfst.append(x)
def dfs2(g,x):
    visited[x] = True
    for y in g.cons[x]:
        if not visited[y]:
           dfs(g,y) 
for x in range(1,n+1):
    if not visited[x]:
        dfs(g,x)
def reverseEdge(g):
    gr = graph(g.v)
    for x in g.cons.keys():
        for j in g.cons[x]:
            gr.addEdge(j,x,'d')
    return gr
gr = reverseEdge(g)
visited = [False]*(n+1)
ans = 0
dfst.reverse()
for x in dfst:
    if not visited[x]:
        dfs2(gr,x)
        ans+=1
print(ans)