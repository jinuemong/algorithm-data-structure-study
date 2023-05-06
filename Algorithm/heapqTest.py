
# 최대 힙
from heapq import heappush, heappop


nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
  heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
  print(heappop(heap)[1])  # index 1

