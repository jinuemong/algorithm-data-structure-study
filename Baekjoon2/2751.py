
# 수 정렬
# n의 수가 최대 100만개이므로, O(NlogN)의 정렬 알고리즘을 사용해야 함

#1. 파이썬 기본 정렬 알고리즘 사용
import sys
n = int(sys.stdin.readline())
n_list = list()

for _ in range(n):
    x = int(sys.stdin.readline())
    n_list.append(x)
n_list.sort()
for n in n_list:
    print(n)

