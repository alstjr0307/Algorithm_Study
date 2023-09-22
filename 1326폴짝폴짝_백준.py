import sys
from collections import deque
n = int(input())
bridge = list(map(int,sys.stdin.readline().split()))
a, b = map(int,input().split())
lens = len(bridge)
a-=1
b-=1
stack = deque()
stack.append(a)
count=0
answer=-1
visit=[_ for _ in range(lens)]
visit.remove(a)
while stack:
    count+=1
    nod = stack.popleft()
    if abs(b-nod) % bridge[nod] ==0:
        answer=count
        break
    for i in visit:
        if abs(nod-i)%bridge[nod]==0:
            stack.append(i)
            visit.remove(i)
print(answer)
            
    
    
    