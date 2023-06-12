

# 기사 단원의 무기
# 약수의 수가 데미지
# 약수는 제곱근까지만 구해도 됨
# limit를 넘을 경우 power로 적용

from math import sqrt
def solution(number, limit, power):
    answer = 1
    for n in range(2,number+1):
        sum = find(n)
        if sum > limit:
            sum = power
        answer+=sum
    return answer

def find(data):
    data_set = set()
    for i in range(1,int(sqrt(data))+1):
        if data%i==0:
            data_set.add(int(data/i))
            data_set.add(i)
    return len(data_set)


number =10
limit = 3
power= 2
print(solution(number,limit,power))