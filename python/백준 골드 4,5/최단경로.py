import heapq
import sys

input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v + 1)]
result = [float("INF") for _ in range(v + 1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    result[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if result[now] < dist:
            continue

        for d, next in graph[now]:
            next_dist = dist + d
            if next_dist < result[next]:
                result[next] = next_dist
                heapq.heappush(q, (next_dist, next))


dijkstra(k)
for i in result[1:]:
    if i == float("INF"):
        print("INF")
    else:
        print(i)
