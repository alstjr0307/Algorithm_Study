imsi = input()
s =[]
answer=0
for i in imsi:
    s.append(int(i))

lens = len(s)
for i in range(lens-1):
    for j in range(min(i+1,lens-i-1)):
        if sum(s[i-j:i+1]) == sum(s[i+1:i+j+2]):
            
            answer = max(answer,j+1)
print(answer*2)