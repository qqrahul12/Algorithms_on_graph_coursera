from collections import defaultdict,deque
graph = defaultdict(list)
n,m = [int(i) for i in input().split()]
for i in range(m):
    x,y = [int(i)-1 for i in input().split()]
    graph[x].append(y)
    graph[y].append(x)
u,v = [int(i)-1 for i in input().split()]
visited = [False]*n
distance = [0]*n
distance[u] = 0
q = deque()
q.append(u)
visited[u] = True
while q:
    x = q.popleft()
    for y in graph[x]:
        if not visited[y]:
            q.append(y)
            distance[y] = distance[x]+1
            visited[y] = True
if  visited[v]:
    print(distance[v])
else:
    print("-1")