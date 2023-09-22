import sys

n = int(input())
data = list(map(int,sys.stdin.readline().split()))
stack = []
answer= [0 for _ in range(n)]
for i in range(n):
    while stack:
        if data[stack[-1][0]]<data[i]:
            stack.pop()
        else:
            answer[i] = stack[-1][0]+1
            break
    stack.append((i,data[i]))

print(*answer)