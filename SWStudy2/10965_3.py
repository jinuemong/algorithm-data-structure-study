

# 10 * 7 의 제곱근 까지 구해야함

# 제곱근 이상의 수 중 소수로 더 이상 나눌 수 없으면 소수
# 에라토스테네스의 체 알고리즘 사용
# 이미 제곱수라면 결과는 1
# 제곱수가 아닌 경우 동일한 소수로 나누는 횟수가 홀수인 경우
# 해당 소수를 곱하면 제곱 수가 됨
# -> 제곱수는 소수의 곱으로 이루어짐
# -> 횟수가 홀수인 경우 A를 곱했을 때 제곱수가 됨
from math import sqrt

max_n = int(sqrt(10**7))
array = [True for _ in range(max_n+1)]

for i in range(2, int(max_n**0.5) + 1):
    if array[i]:
        # 에라토스테네스의 체 사용
        # 해당 수가 소수가 아니라면 그 수의 곱도 소수가 아님
        j = 2
        while i * j <= max_n:
            array[i * j] = False
            j +=1
# 소수 리스트
prime = []
for i in range(2,len(array)):
    if array[i]:
        prime.append(i)

result = []

for t in range(int(input())):
    n = int(input())
    answer = 1

    if sqrt(n) != int(sqrt(n)): #이미 배수인지 확인
        for p in prime:
            count = 0
            while n% p == 0:
                n//=p
                count+=1
            if count % 2 != 0: # 홀수 확인
                answer *=p
            if n == 1 or p > n:
                break
        if n>1:
            answer *= n
    result.append(answer)

for i in range(len(result)):
    print(f"#{i+1} {result[i]}")