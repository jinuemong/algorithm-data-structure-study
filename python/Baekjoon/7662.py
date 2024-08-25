# https://www.acmicpc.net/problem/7662
import heapq

# I n : n을 Q에 삽입
# D 1 : 최댓값 삭제
# D -1 : 최솟값 삭제
# 비어있는 경우 D 연산 무시
# o(N) 시간 복잡도 풀어야함
t = int(input())

for _ in range(t):
    min_heap,max_heap = [],[]

    k = int(input())
    for _ in range(k):
        a = list(input().split())

        if a[0]=="I":
            heapq.heappush(max_heap,(-int(a[1])))
            heapq.heappush(min_heap, (int(a[1])))
        elif a[0]=="D":
            if len(min_heap)>0 and len(max_heap)>0:
                if a[1]=="1":
                    pp = heapq.heappop(max_heap)
                    min_heap.remove(-pp)
                if a[1]=="-1":
                    pp = heapq.heappop(min_heap)
                    max_heap.remove(-pp)

    if len(max_heap)>0:
        print(-heapq.heappop(max_heap), heapq.heappop(min_heap))
    else:
        print("EMPTY")
