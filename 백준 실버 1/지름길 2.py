

## 지름길
import heapq

n,d = list(map(int,input().split()))
INF = 1e8

graph = [[] for i in range(d+1)]
for i in range(d):
    graph[i].append((i+1,1))
distance = [INF] * (d+1)

for _ in range(n):
    u,v,w = map(int,input().split()) # v는 목적지, w는 가중치
    if v> d: continue # 목적지가 더 큰 경우 제외
    graph[u].append((v,w))

def dijkstra():
    q = []
    heapq.heappush(q,(0,0))
    distance[0] = 0

    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            new_w = dist + i[1]
            # distance[i[0]] : prev w

            if new_w < distance[i[0]]:
                distance[i[0]] = new_w
                heapq.heappush(q,(i[0],new_w))

dijkstra()
print(distance[d])