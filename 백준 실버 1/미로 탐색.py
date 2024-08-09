from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, list(input()))) for i in range(n)]

queue = deque([(0,0)])
while queue:
    a, b = queue.popleft()
    for x, y in ((a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1)):
        if 0<=x<n and 0<=y<m and graph[x][y] != 0 and graph[x][y] == 1:
            graph[x][y] = graph[a][b]+1
            queue.append((x,y))
print(graph[n-1][m-1])
