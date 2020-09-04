from collections import defaultdict,deque
graph = defaultdict(list)
n,m = [int(i) for i in input().split()]
for i in range(m):
    x,y = [int(i)-1 for i in input().split()]
    graph[x].append(y)
    graph[y].append(x)
colored = [-1]*n
q = deque()
def check_bipertite():
    while q:
        x = q.popleft()
        for y in graph[x]:
            if colored[y]==-1:
                colored[y] = 1 - colored[x]
                q.append(y)
            elif colored[y]==colored[x]:
                return False
    return True 
ans = True
for i in range(n):
    if colored[i]==-1:
        q.append(i)
        colored[i] = 1
        tmp = check_bipertite()
        if not tmp:
            ans = False
if ans:
    print("1")
else:
    print("0")