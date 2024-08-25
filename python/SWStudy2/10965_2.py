
# 10965 : 제곱수 만들기

# 2번째 시도

# 어떤 자연수의 제곱 = A * result
# 만족하는 최소의 result를 구하라
# k*k = n*result
# k*k/A = result를 만족

# a = 1
# k = 1 인 경우
# result = 1

# a =2
# k = 1 인 경우
# reuslt = 1/2 -> false

# a = 2
# k = 2 인 경우
# result = 2 -> true

# result를 정의 result = k*k/A
# result를 정수로 만드는 k값이 나올 때 까지 k 증가
# result 의 최소는 1
# A = k*k
# 즉 k 는 sqrt(A)부터 탐색

# 모든 테스트 케이스 마다 반복해서 소수를 구하면 비효율적
# 소수에 대해서만 A가 나누어 떨어지는지 확인

from math import sqrt
# prime : 소수 리스트
max_len = int(sqrt(10**7)+1)
prime = [True for _ in range(max_len)]

for i in range(2, int(max_len)):
    if prime[i]:
        j = 2
        while i*j <= max_len:
            prime[i*j] = False
            j += 1
print(prime)

answer = []
for t in range(int(input())):
    A = int(input())
    k = 1
    if type(sqrt(A)) != int: # true인 경우 result = 1
        for p in prime:
            cnt = 0
            while not A% p :
                A //= p
                cnt+=1
            if cnt % 2:
                k *=p
            if A == 1 or p > A:
                break
        if A > 1:
            k *= A
    answer.append(f"#{t+1} {k}")
for a in answer:
    print(a)