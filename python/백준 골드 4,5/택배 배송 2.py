# 다익스트라 적용하기
# 각 노드의 최소값 적용

import heapq
import sys

INF = sys.maxsize
n, m = map(int, input().split())
distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]  # 1번 ~ n번 노드
for _ in range(m):
    u, v, w = map(int, input().split())  # 각 출발, 도착, 가중치
    graph[u].append((v, w))  # 목적지, 가중치 입력
    graph[v].append((u,w))


def dia(start):
    q = []
    heapq.heappush(q, (0,start)) # 1번 노드로 0 이동
    distance[start] = 0 # 1번 노드로 이동은 0
    while q: # 1번노드와 연결된 노드 탐색
        dist, now = heapq.heappop(q) # 거리, 현재 노드 팝
        if distance[now] < dist:  # 큰 값만 탐색
            continue
        for v,w  in graph[now]: # 목적지, 가중치 팝
            new_w = dist + w
            if new_w < distance[v]:  # 더 큰 값 발견
                distance[v] = new_w
                heapq.heappush(q,(new_w, v))


dia(1)
print(distance[n])
