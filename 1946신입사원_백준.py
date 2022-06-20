t= int(input())
answer=[]
for test in range(t):
    n = int(input())
    ans=1
    a=[]
    for i in range(n):
        t,f =map(int,input().split())
        a.append([t,f])
    sorta= sorted(a, key = lambda x:x[0])
    min = sorta[0][1]

    for i in range(1,n):
        if sorta[i][1]<min:
            ans+=1
            min = sorta[i][1]
            
    answer.append(ans)
for i in answer:
    print(i)