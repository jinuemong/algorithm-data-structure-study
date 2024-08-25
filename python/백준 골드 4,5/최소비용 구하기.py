import sys
import heapq
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = {i: [] for i in range(1, n + 1)}
value = [ float("inf") for _ in range(n+1)]
for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
start, end = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    value[start] = 0

    while q:
        w,v = heapq.heappop(q)
        if value[v] < w:
            continue
        for dw,dv in graph[v]:
            if w + dw < value[dv]:
                value[dv] = w + dw
                heapq.heappush(q,(w+dw,dv))

dijkstra(start)
print(value[end])