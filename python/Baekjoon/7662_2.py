# https://www.acmicpc.net/problem/7662
import heapq

# I n : n을 Q에 삽입
# D 1 : 최댓값 삭제
# D -1 : 최솟값 삭제
# 비어있는 경우 D 연산 무시
# o(N) 시간 복잡도 풀어야함
t = int(input())


def pop(heap):
    while len(heap) > 0:
        data, id = heapq.heappop(heap)
        if not deleted[id]:
            deleted[id] = True
            return data
    return False


for _ in range(t):
    min_heap, max_heap = [], []
    k = int(input())
    current = 0
    deleted = [False] * (k + 1)
    for _ in range(k):
        a = list(input().split())

        if a[0] == "I":
            heapq.heappush(max_heap, (-int(a[1]), current))
            heapq.heappush(min_heap, (int(a[1]), current))
            current +=1
        elif a[0] == "D":
            if len(min_heap) > 0 and len(max_heap) > 0:
                if a[1] == "1":
                    pop(max_heap)
                if a[1] == "-1":
                    pop(min_heap)
    x = pop(max_heap)
    if x:
        heapq.heappush(min_heap,(-x,current))
        print(-x, pop(min_heap))
    else:
        print("EMPTY")
