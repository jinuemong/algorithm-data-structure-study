import heapq
n, e = map(int,input().split())
graph = {i+1:[] for i in range(n)}

for i in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a, c))
v1,v2 = map(int,input().split())

def search(start,end):
    visited = [float("inf") for _ in range(n+1)]
    q = []
    heapq.heappush(q,(0,start))
    visited[start] = 0

    while q:
        d, prev = heapq.heappop(q)
        if visited[prev] < d:
            continue
        if prev == end:
            return d
        for current in graph[prev]:
            next = d + current[1]
            if next < visited[current[0]]:
                visited[current[0]] = next
                heapq.heappush(q,(next,current[0]))
    return float("inf")

v1_search = search(1,v1)+search(v1,v2)+search(v2,n)
v2_search = search(1,v2)+search(v2,v1)+search(v1,n)
result = min(v2_search,v1_search)
if result == float("inf"):
    print(-1)
else:
    print(result)