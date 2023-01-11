from collections import deque
import sys
n,m=map(int,input().split())
data=[[] for _ in range(n+1)]
for i in range(m):
    a, b= map(int,input().split())
    data[a].append(b)
    data[b].append(a)
maxx=sys.maxsize
answer=[maxx for _ in range(n+1)]
def bfs(root,graph):
    global answer
    visit = [root]
    num = [0 for _ in range(n+1)]
    queue= deque([root])

    while queue:
        t = queue.popleft()
    
        for i in graph[t]:
            if i not in visit:
                queue.append(i)
                visit.append(i)
                num[i] +=num[t]+1
                if len(visit)==n:
                    answer[root]  = sum(num)
    

for i in range(1,n+1):
    bfs(i,data)
t = min(answer)
print(answer.index(t))