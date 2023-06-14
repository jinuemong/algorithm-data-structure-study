def solution(n):
    num = set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i)) #배수 모두 제거 


n = 5
print(solution(n))