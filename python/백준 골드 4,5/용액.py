#  0   1  2 3  4  5
# -99 -2 -1 4 98 150
import heapq

n = int(input())
n_list = list(map(int, input().split()))
heap = []

start, end = 0, n - 1

while start < end:
    s = n_list[start] + n_list[end]
    heapq.heappush(heap, (abs(s), start, end))
    if s >= heap[0][0]:
        end -=1
    else:
        start += 1
print(n_list[heap[0][1]],n_list[heap[0][2]])
