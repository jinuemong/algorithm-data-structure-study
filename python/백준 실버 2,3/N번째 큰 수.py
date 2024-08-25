import heapq

n = int(input())
heap = list(map(int, input().split()))
heapq.heapify(heap)
for _ in range(n - 1):
    numbers = map(int, input().split())
    for number in numbers:
        if heap[0] < number:
            heapq.heappop(heap)
            heapq.heappush(heap, number)
print(heap[0])
