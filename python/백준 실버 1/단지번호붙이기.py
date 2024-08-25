from collections import deque

n = int(input())

graph = [list(map(int, input())) for j in range(n)]

visited = [[0 for _ in range(n)] for _ in range(n)]
result = []
for i in range(n):
    for j in range(n):
        if visited[i][j] or graph[i][j] == 0:
            continue
        current = 1
        queue = deque([(i,j)])
        visited[i][j] = 1
        while queue:
            a,b = queue.popleft()
            for x,y in ((a-1,b),(a+1,b),(a,b+1),(a,b-1)):
                if n>x>=0 and n>y>= 0 and not visited[x][y] and graph[x][y]:
                    current+=1
                    visited[x][y] = 1
                    queue.append((x,y))
        if current>0:
            result.append(current)
            current = 0
print(len(result))
for r in sorted(result):
    print(r)







