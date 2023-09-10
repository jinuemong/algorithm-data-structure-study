import math


def solution(arr):
    n = arr[0]
    for i in arr[1:]:
        n = lcm_2(n,i)
    return n

# 두 자연수의 곱 / 최대 공약수
def lcm(a,b):
    return a*b // math.gcd(a,b)
# math를 활용한 최대 공약수 구하기
def lcm_2(a,b):
    return math.lcm(a,b)
print(solution([2,6,8,14]))