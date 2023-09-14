n = int(input())
data=[]
for i in range(n): 
    data.append(int(input()))
data.sort(reverse=True)
answer=0
i=0
while i<n-1:
    print(i)
    if data[i] *data[i+1] > data[i]+data[i+1]:
        answer+=data[i]*data[i+1]
        i+=2
        
        
    else:
        answer+=data[i]
        i+=1

print(answer)