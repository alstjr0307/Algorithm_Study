t= int(input())
answeer=[]
for test in range(t):
    x, y = map(int,input().split())
    gap = y-x
    a=0
    b=1
    high=0
    
    while True:
        a+=1
        high+=a

        if high*2>=gap:
            go =(((high*2)-1 + (high-a+1)*2)/2)
            if float(gap) <go:

                answer = (2*a)-1

            else: answer = 2*a
            break
    answeer.append(answer)
for i in answeer:
    print(i)
