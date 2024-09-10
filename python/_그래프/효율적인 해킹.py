from collections import deque
n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
result = [1 for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

max_count = 0
def bfs(start):
    global max_count
    queue = deque([start])
    visited = [0 for _ in range(n+1)]
    visited[start] = 1
    count = 1
    while queue:
        current = queue.popleft()
        for i in graph[current]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)
                count+=1
    max_count = max(count,max_count)
    return count

for i in range(1,n+1):
    result[i] = bfs(i)
for i in range(1,n+1):
    if result[i] == max_count:
        print(i,end = " ")

