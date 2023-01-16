T = int(input())
data =[]
for i in range(0,T):
    data.append(list(map(int,input().split(' '))))
answer=[]
for i in range(0,T):

    #중심 간 거리 제곱
    dist=(data[i][3] - data[i][0])^2 +(data[i][4] - data[i][1])^2
    #반지름 합 제곱
    rad_sum = (data[i][2] +data[i][5])^2


    #아예 같은 원
    if data[i][0]==data[i][3] and data[i][1]==data[i][4] and data[i][2]==data[i][5]:
        answer.append(-1)
    #중심 같고 다른 원
    elif data[i][0]==data[i][3] and data[i][1]==data[i][4] and data[i][2] != data[i][5]:
        answer.append(0)

    #큰 원 안에 작은 원, 
    elif dist<max(data[i][2],data[i][5])**2:
        if max(data[i][2], data[i][5])> dist**(1/2) + min(data[i][2], data[i][5]):
            answer.append(0)
        elif dist<max(data[i][2],data[i][5])**2 and  max(data[i][2], data[i][5])== dist**(1/2) + min(data[i][2], data[i][5]):
            answer.append(1)
        elif  dist<max(data[i][2],data[i][5])**2 and  max(data[i][2], data[i][5])< dist**(1/2) + min(data[i][2], data[i][5]):
            answer.append(2)
    # 아예 안만나는 경우
    elif dist>rad_sum:
        answer.append(0)
    
    #원 두개가 맞닿은 경우
    elif dist==rad_sum:
        answer.append(1)
    elif dist<rad_sum:
        answer.append(2)

for i in answer:
    print(i)