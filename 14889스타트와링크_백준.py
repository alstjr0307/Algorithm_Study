import sys
n= int(input())
data=[]

answer=sys.maxsize
for i in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    data.append(a)
visited=[]
start=0
def dfs(idx, cnt):
    global answer
    global select
    if cnt ==n//2:
        start,link=0,0
        for i in range(n):
            for j in range(n):
                if select[i] and select[j]:
                    start+=data[i][j]
                elif not select[i] and not select[j]:
                    link+=data[i][j]

        answer= min(answer,abs(start-link))
    for i in range(idx, n):
        if select[i]:
            continue
        select[i]=1
        dfs(i+1, cnt+1)
        select[i]=0

select=[0 for i in range(n)]
dfs(0,0)
print(answer)


