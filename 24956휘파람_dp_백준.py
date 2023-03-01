import sys
sys.setrecursionlimit(1000000000)
n = int(input())
s= sys.stdin.readline()
answer=0

dpw = [0 for _ in range(n+1)]
dpe = [0 for _ in range(n+1)]
answer=0
cnt=0
for i in range(n):
    dpw[i] = dpw[i-1]
    dpe[n-i-1] = dpe[n-i]
    if s[i] == 'W':
        dpw[i]= dpw[i-1]+1
    
    if s[n-i-1] == 'E':
        dpe[n-i-1]= (dpe[n-i]*2 +cnt) %1000000007
        cnt+=1

for i in range(n):
    if s[i] == 'H':
        answer += (dpw[i] *dpe[i])
        answer%=1000000007

print(answer)
