from collections import deque
n, m ,v= map(int,input().split())
data=[[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int,input().split())
    data[a].append(b)
    data[b].append(a)
for i in data:
    i.sort()
visit=[]
answer=[]
def dfs(start, graph, visit):
    global answer
    visit.append(start)
    if len(visit) == n:
        answer.append(visit)
        return
    for i in graph[start]:
        if i not in visit:
            dfs(i,graph,visit)
visit2=[]
def bfs():
    queue = deque([v])
    visit2.append(v)
    while queue:
        a = queue.popleft()
        for i in data[a]:
            if i not in visit2:
                queue.append(i)
                visit2.append(i)




dfs(v,data,visit)
bfs()
print(' '.join(map(str,visit)))
print(' '.join(map(str,visit2)))


    
