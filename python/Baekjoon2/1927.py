
# 최소 힙
from heapq import heappop,heappush
import sys
heap = []

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    data = int(sys.stdin.readline().rstrip())

    if data ==0:
        if heap:
            print(heappop(heap))
        else:
            print(0)
    else:
        heappush(heap,data)

