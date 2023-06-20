
import math
def solution(n, k):
    answer = 0
    for i in [int(i) for i in make_jinsu(n,k,"").split("0") if i != '']:
        answer+=check_prime(i)
    return answer

# 진수 만들기
def make_jinsu(number,k,data):
    while number>0:
        data = str(number%k) + data
        number = int(number/k)
    return data

# 변환수가 소수인지 확인
def check_prime(pn):
    if pn ==1:
        return 0
    for i in range(2,int(math.sqrt(pn))+1):
        if pn%i==0:
            return 0
    return 1





n = 110011
k = 10
print(solution(n,k))
