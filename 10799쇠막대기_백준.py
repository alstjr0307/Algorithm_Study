data=list(input())
lens = len(data)
answer=0
left=0
stick=[]
for i in range(lens):
    if data[i]=='(':
        stick.append('(')
    else:
        if data[i-1]=='(':
            stick.pop()
            answer+=len(stick)
        else:
            stick.pop()
            answer+=1
print(answer)

