n = int(input())
data=[]
for i in range(n):
    data.append(int(input()))
key=1
value=1
answer=[]
imsi=[]
for i in data:
    while key<=i:
        imsi.append(key)
        answer.append('+')
        key+=1
    if imsi[-1] == i:
        answer.append('-')
        imsi.pop()
    else:
        print('NO')
        exit()
for i in answer:
    print(i)


    
