a, b, c = map(int,input().split())
#분할정복 문제


#지수 법칙
#A^m+n = A^m x A^n

#나머지 분배 법칙
#(AxB)%C = (A%C) *(B%C) % C

def calculate(a,mid):
    if mid ==1:
        return a%c

    tmp = calculate(a,mid//2)
    if mid%2==1:
        return (tmp *tmp*a)%c
    else:  
        return (tmp*tmp)%c
print(calculate(a,b))
        