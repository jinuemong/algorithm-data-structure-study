
# 피보나치 수
# Fn = Fn-1 + Fn-2

# 1. 피보나치 수열의 점화식 세우기
# f0 = 0, f1=  1
# fn = fn-1 + fn-2 (n>=2)
# 2. 재귀 함수를 이용해 문제를 풀 수 있는지 검토
# 3. N의 최대 값은 45


# 재귀함수의 실패 코드
# 정상 통과지만 시간 초과 발생
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n -2)

# -> 반복적으로 동읾한 형이 여러번 호출 됨
# O(2 - n제곱 )

n = int(input())
a,b = 0,1
while n> 0:
    a,b = b, a+b
    n-=1
print(a)
