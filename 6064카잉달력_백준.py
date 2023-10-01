import math
t= int(input())
answer=[]
for i in range(t):
    m, n ,x, y = map(int,input().split())
    lcm = math.lcm(m,n)
    flag=0
    if x ==y:
        answer.append(x)
    else:
        if x<y:
            tmp= x
        
            while tmp<=lcm:
                if (tmp-y)% n ==0:
                    answer.append(tmp)
                    flag=1
                    break
                else:
                    tmp+=m
        else:
            tmp = y
            while tmp<=lcm:
                if  (tmp-x)% m ==0:
                    answer.append(tmp)
                    flag=1
                    break
                else:
                    tmp+=n
        if flag==0:
            answer.append(-1)

for i in answer:
    print(i)
    
            
    