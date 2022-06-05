n, m = map(int,input().split())
data=[]
data2=[]
for i in range(n):
    data.append(input())
for i in range(m):
    data2.append(input())
answer= set(data) & set(data2)
print(len(answer))
answer=list(answer)
answer.sort()
for i in answer:
    print(i)