import sys
maxx= sys.maxsize
n, k = map(int,input().split())
dp=[0 for _ in range(0,k+1)]

data=[]
for i in range(n):
    ims=int(input())
    data.append(ims)
    if ims<=k:
        dp[ims]=1
data.sort()

for i in range(2,k+1):
    
    if dp[i] ==0:
        imsi = maxx
        flag=0
        for j in range(1,(i+1)//2+1):
            
            if dp[j]!=0 and dp[i-j]!=0:
                imsi= min(imsi, dp[j]+dp[i-j])
                flag=1
        if flag==1:
            dp[i] =imsi


if dp[k]==0:
    print(-1)
else:print(dp[k])
    