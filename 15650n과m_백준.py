n,m= map(int,input().split())
visited=[]
need_visit=[i for i in range(1,n+1)]
answer=[]
imsi=[]
def dfs(start,visited,len):
    global answer
    visited.append(start)
    imsi.append(start)
    if len(imsi)==m:
        answer.append(imsi)
        imsi.pop()
    else:
        for i in range(start+1, n+1):
            if i not in visited:
                dfs(i,visited,len)
    
dfs(1,visited,m)