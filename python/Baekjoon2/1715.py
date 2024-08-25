
# 카드 정렬하기

# 두 묶음의 숫자 카드
# A+B 번의 비교하여 하나로 만듦
# 최소힙으로 해결해야 하는 문제
# 카드 묶음이 크기에 따라 정렬되어 있다면
# 비교 횟수가 가장 적음

from heapq import heappop,heappush
import sys
n = int(sys.stdin.readline().rstrip())

heap = []

for _ in range(n):

    heappush(heap,int(sys.stdin.readline().rstrip()))

result = 0

while len(heap) != 1:
    one = heappop(heap)
    two = heappop(heap)

    sum_value = one+ two
    result += sum_value
    heappush(heap,sum_value)
print(result)