import sys

n = int(input())
data = list(map(int,sys.stdin.readline().split()))
data.reverse()
top = max(data)
data2=[]
for i in data:
    data2.append(top-i)

answer=[]
flag=0

start=data2[0]
if n==1:
    answer2=[0]

else:
        
    while flag<=n-1:
        
        tmp=1
        flag+=1
        if flag<n:
            while data2[flag] >=start :
                tmp+=1
                flag+=1
                if flag >=n:
                    break
        
            for i in range(tmp):
                answer.append(flag)
            if flag<n:
                start = data2[flag]
            else:
                break
        else:
            answer.append(flag)
            
        
    answer2=[]
    answer.reverse()
    for i in answer:
        answer2.append(n-i)
for i in range(n-1):
    print(answer2[i], end=" ")
print(answer2[-1])