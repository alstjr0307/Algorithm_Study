from itertools import combinations as combi
n = int(input())

chars=['9','8','7','6','5','4','3','2','1','0']
alls=[]
for i in range(1,11):
    tmp = combi(chars,i)

    for j in list(tmp):

        alls.append(int(''.join(j)))
alls.sort()

try: print(alls[n])
except: print(-1)