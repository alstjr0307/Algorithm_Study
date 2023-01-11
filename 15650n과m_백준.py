n,m= map(int,input().split())
visited=[]
need_visit=[i for i in range(1,n+1)]
answer=[]
imsi=[]
def dfs(start):
    global answer
    if len(visited)==m:
        print(' '.join(map(str,visited)))
        return
    for i in range(start, n+1):
        if i not in visited:
            visited.append(i)
            dfs(i)
            visited.pop()
dfs(1)
