

# 콜라 문제

# a개의 콜라를 가져가면 , b개의 콜라는 주는 마트가 있다
# n개의 콜라를 가져갔을 때, 몇개의 콜라를 받을 수 있나

def solution(a, b, n):
    answer = 0
    count = 0
    while n>1:
        k = int(n/a)
        n =(k*b + int(n%a))
        answer+=k*b
        print(k,n)
        count+=1
        if k==0:
            break

    return answer
a = 3
b = 1
n = 20

print(solution(a,b,n))