
from math import sqrt
# 10965 제곱수 만들기

# 자연수 A가 주어졌을 때
# B를 곱한 결과가 거듭제곱수가 되는 최소의 B를 구하라
#  n * result = 최소의 거듭 제곱 수
#  k*k < n * result < (k+1)*(k+1)
#  k*k / n < result < (k+1)*(k+1) / n
#  k*k = n 인 값 부터 탐색
#  k = 루트(n)-1 인 정수 부터 +1씩 하면서 탐색
#  를 만족하는 result를 찾아라

for t in range(int(input())):
    n = int(input())
    k = 1
    while True:
        if (k*k)%n==0:
            print(f"#{t+1} {int(k/n)}")
            break
        k+=1