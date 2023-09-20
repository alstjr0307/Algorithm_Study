import math

infi = math.inf

n = int(input())
data= list(map(int,input().split()))
maxx= 0

for i in range(len(data)):
    flag = 0
    obstacle = [i,-infi,i,-infi]
    ims = [0,0]
    while True:
       
        flag +=1
        if i+flag < n:
            if obstacle[0] == i :
                ims[0]+=1
                
            elif data[i] +(obstacle[1]* (flag))<data[i+flag]:
                ims[0]+=1
            if (data[i+flag]-data[i])/flag >obstacle[1]:
                obstacle[1] = (data[i+flag]-data[i])/flag
                obstacle[0] = i+flag

        if i - flag>=0:
            if obstacle[2] == i:
                ims[1]+=1
            elif data[i] +(obstacle[3] * (flag))<data[i-flag]:
                ims[1]+=1
            if obstacle[3] < (data[i-flag]-data[i])/flag:
                obstacle[3] = (data[i-flag] -data[i])/flag
                obstacle[2] = i-flag
    
        if i+flag>=n and i-flag<0:
            maxx= max(maxx, sum(ims))
            break
print(maxx)

        
        
        
            