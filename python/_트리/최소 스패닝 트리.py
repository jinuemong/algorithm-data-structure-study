import heapq

v, e = map(int, input().split())

heap = [(0,1)]
graph = [[] for _ in range(v + 1)]
visited = [0] * (v + 1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

result = 0
cnt = 0

while heap:
    if cnt == v:
        break

    current_w,current_v = heapq.heappop(heap)

    if not visited[current_v]:
        visited[current_v] = 1
        result += current_w
        cnt +=1
        for next in graph[current_v]:
            heapq.heappush(heap,next)
print(result)