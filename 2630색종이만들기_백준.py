n= int(input())
paper=[]
for i in range(n):
    paper.append(list(map(int,input().split())))

zero=0
one=0

def check(data):
    global zero
    global one
    lens = len(data)
    tmp=data[0][0]
    for i in range(len(data)):
        if (1-tmp) in data[i]:
            a = [data[t][:lens//2] for t in range(lens//2)]
            b= [data[t][lens//2:lens] for t in range(lens//2,lens)]
            c = [data[t][:lens//2] for t in range(lens//2,lens)]
            d =[data[t][lens//2:lens] for t in range(lens//2)]
            check(a)
            check(b)
            check(c)
            check(d)
            break
    else:
        if tmp == 0:
            zero+=1
        else: one+=1

check(paper)
print(zero)
print(one)
    