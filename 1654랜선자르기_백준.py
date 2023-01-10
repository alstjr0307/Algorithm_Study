k,n = map(int,input().split())
data=[]
for i in range(k):
    data.append(int(input()))

data.sort()
start=1
end=data[-1]
sum=0
again=0
while start<=end:
    
    mid = (start+end)//2
    if mid==0: mid=1
    sum=0
    for i in data:
        sum+=i//mid

    if sum<n:
        end= mid-1
        
    if sum>=n:
        again+=1
        start=mid+1
    mid = (start+end)//2
print(mid)        