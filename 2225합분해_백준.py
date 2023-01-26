n,k = map(int,input().split())
all=[]
dp = [1 for _ in range(1,n+1)]
all.append(dp)
if n ==1:
    print(k)

else:
    for i in range(k-1):
        ims = [0 for _ in range(1,n+1)]
        for j in 