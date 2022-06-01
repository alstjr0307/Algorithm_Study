from itertools import permutations
def check(a,b): #a와 b가 같은 유저인지 판별하는 함수
    cnt=0
    if len(a)!=len(b):
        return False
    for i in range(len(a)):
        if a[i] == b[i] or b[i] =='*':
            cnt+=1
    if cnt == len(a):
        return True
    else: return False

def solution(user_id, banned_id):
    answer=[]
    for i in permutations(user_id, len(banned_id)): #permutaion 함수는 a리스트에서 b개를 포함하는 조합을 만들어줌

        count=0
        for a,b in zip(i,banned_id):

            if check(a,b):
                count+=1
        if count == len(banned_id):
            if set(i) not in answer: #아이디 순서에 상관 없다했으므로 set 사용
                answer.append(set(i))
 
    return len(answer)
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"])