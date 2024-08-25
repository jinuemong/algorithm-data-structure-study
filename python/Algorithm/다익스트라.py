
n,m = map(int,input().split())
k = int(input()) # 시작 노드
INF = 1e8

graph = [[] for _ in range(n+1)] # 1번 ~ n번 노드

distance = [INF] * (n+1)

for _ in range(m):
    u,v,w = map(int,input().split()) # 각 출발, 도착, 가중치
    graph[u].append((v,w)) # 목적지, 가중치 입력

import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q,(start,0)) # 자기 자신이 목적지인 경우 가중치 0
    distance[start] = 0

    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist: # 이미 입력 값이 현재 노드 거리보다 더 작다면 생략
            continue

        for i in graph[now]: # 모든 연결 노드 탐색
            if dist + i[1] < distance[i[0]]: # 기존 입력 값이 크면 교체
                # i[0] -> 목적지, i[1] -> 가중치
                distance[i[0]] = dist + i[1]
                heapq.heappush(q,(i[0],dist+i[1]))

dijkstra(k)
print(graph)
print(distance)

# 5 6
# 1
# 5 1 1
# 1 2 1
# 1 3 3
# 2 3 1
# 2 4 5
# 3 4 2