from itertools import combinations as combi

#combi 함수 활용과 discard함수의 활용


def solution(relation):
    answer = 0
    candi=[]
    types = len(relation[0])
    students= len(relation)
    candidates=[]
    for i in range(1,types+1):
        candidates.extend(combi(range(types),i))
    
    unique=[]
    for i in candidates:
        tmp = [tuple([item[j] for j in i]) for item in relation]
        if len(set(tmp)) == students:
            unique.append(i)
    answer=set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
    print(answer)
    return len(answer)

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])