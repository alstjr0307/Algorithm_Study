import sys
sys.setrecursionlimit(1000000000)
n = int(input())
s= input()
answer=0
words=['W','H','E','E']
def dfs(k,word):
    global answer
    if s[k] ==words[word] and k<=n-1:
        if word ==0:
            for j in range(k+1,n):
                dfs(j,word+1)
        elif word ==1:
            for j in range(k+1,n):
                dfs(j,word+1)
        elif word ==2:
            for j in range(k+1,n):
                dfs(j,word+1)
        else:
            answer+=1
            return
    elif k<n-1:
        dfs(k+1,word)
    else:
        return
if n>=4:
    for i in range(0,n-3):
        dfs(i,0)
else:
    answer=0
answer=answer%1000000007
print(answer)


        
