from collections import deque

n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def find(start):
    current_graph = graph.copy()
    visited = [0 for _ in range(n + 1)]
    visited[start], visited[0] = -1, -1
    stack = deque(current_graph[start])
    depth = 1
    while stack:
        next = []
        for value in stack:
            if visited[value] == 0:
                next += current_graph[value]
                visited[value] = depth
        stack = next
        depth += 1
    return sum(visited) + 2

min_idx,min_value = 0, float("inf")
for i in range(1, n + 1):
    find_i = find(i)
    if min_value > find_i:
        min_idx, min_value = i,find_i
print(min_idx)
