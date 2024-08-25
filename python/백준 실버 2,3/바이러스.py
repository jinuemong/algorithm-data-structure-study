from collections import deque

n = int(input())
v = int(input())
graph = [set() for i in range(n + 1)]
visited = [0] * (n + 1)
for i in range(v):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)


def BFS(graph, visited):
    queue = deque([1])
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)  # 방문 기록 빼고 추가
    return len(visited) - visited.count(0)

print(BFS(graph, visited) - 1)
