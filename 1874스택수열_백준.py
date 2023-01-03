n = int(input())
data=[]
for i in range(n):
    data.append(int(input()))
where=data.index(n)
key=0
answer=[]
for i in range(n):
    while True:
        key+=1
        answer.append('+')
        if key==data[n]:
            answer.append('-')
            break
    
for i in range(0, where-1):
    if data[i]
for i in range(where,n-1):
    if data[i]<data[i+1]:
        print('NO')
        exit()

for i in range(n):
