import sys
sys.setrecursionlimit(100000)

def solution(user_id, banned_id):
    answer = 0
    len_ban = len(banned_id)
    visit = [False for _ in range(len_ban)]
    for i in range(len_ban):
        
def dfs(ban,ind,user):
    for i in user:
        if len(ban[ind]) == len(i):
            for j in range(len(i)):
                if i[j] == ban[ind][j] or ban[ind][j]=='*':
                    tmp = user.copy()
                    tmp.remove(i)
                    if i<len(ban):
                        dfs(ban,ind+1,tmp)

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"])