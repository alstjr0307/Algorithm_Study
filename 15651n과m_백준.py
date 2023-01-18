n , m = map(int,input().split())
visit=[]
def dfs():
    if len(visit) == m:
        print(' '.join(map(str,visit)))
        return
    for i in range(1, n+1):
        visit.append(i)
        dfs()
        visit.pop()
dfs()