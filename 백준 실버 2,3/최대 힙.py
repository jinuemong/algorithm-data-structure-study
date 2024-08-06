
import heapq
import sys
input = sys.stdin.readline
queue = []

n = int(input())
for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(queue,(-x))
    else:
        if len(queue) > 0:
            print(-heapq.heappop(queue))
        else:
            print(0)
