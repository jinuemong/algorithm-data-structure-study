
import heapq

heap = []

n,tasu,p = list(map(int,input().split()))
count = 1
if n > 0 :
    arr = list(map(int,input().split()))
    for a in arr:
        if len(heap) < p:
            heapq.heappush(heap, a)
        else:
            if heap[0] < a:
                heapq.heappop(heap)
                heapq.heappush(heap, a)

    if heap[0] < tasu:
        heapq.heappop(heap)
        heapq.heappush(heap, tasu)
        for d in sorted(heap, reverse=True):
            if d == tasu:
                break
            count += 1
        print(count)
    else:
        print(-1)
else :
    print(1)




