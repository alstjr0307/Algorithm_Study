l,c = map(int,input().split())
data= list(input().split())
data.sort()
print(data)
answer=[]
visit=[]
password=[]
n=0
def dfs(n):
    password.append(data[n])
    visit.append(n)
    if len(answer)==l:
        answer.append(password)
        return
    for i in range(n+1,c):
        if i not in visit:
            dfs(i)
            password.pop()
for _ in range(c-l+1):
    dfs(0)
print(answer)