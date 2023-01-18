import math,sys

t= int(input())
data=[]
answer=[]
def sum_num(n):
    sum_n=n*(n+1)//2
    return int(sum_n)

for i in range(t):
    n = int(sys.stdin.readline())
    start=1
    end = n
    mid = (start+end)//2
    while start<=end:
        summ=sum_num(int(mid))
        if summ>n:
            end = mid+1
        elif summ<n:
            start = mid-1
        else:
            answer.append(mid)
            break
        if (start+end)//2 != mid:
            mid = (start+end)//2
        else: 
            answer.append(mid)

            break
for i in answer:
    print(i)