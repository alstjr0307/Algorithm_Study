n=int(input())
left=[0 for _ in range(n)]
right=[0 for _ in range(n)]
no=[0 for _ in range(n)]
left[0]=1
right[0]=1
no[0]=1
for i in range(1,n):
    left[i] = right[i-1]+no[i-1]
    right[i]=left[i-1]+no[i-1]
    no[i]=left[i-1]+right[i-1]+no[i-1]
    left[i] = left[i]%9901
    right[i]=right[i]%9901
    no[i]=no[i]%9901
print((left[n-1]+right[n-1]+no[n-1])%9901)