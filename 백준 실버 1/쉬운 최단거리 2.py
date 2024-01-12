
## 쉬운 최단 거리
# 모든 이동 경로 탐색

## 각 지점으로 이동거리 저장

from collections import  deque
n,m = map(int,input().split())
nm = []
queue = deque([])
visit = [[False]*m for _ in range(n)]
result = [[-1]*m for _ in range(n)]

for i in range(n):
    nm.append(list(map(int,input().split())))
    for j,data in enumerate(nm[-1]):
        if data == 2:
            queue.append((i,j))
            visit[i][j] = True
            result[i][j] = 0
        if data == 0:
            result[i][j] = 0
direction = [(1,0),(-1,0),(0,1),(0,-1)]

while queue:
    x,y = queue.popleft() #앞에서부터 처리

    for dx,dy in direction:
        nx,ny = x+dx,y+dy

        if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and nm[nx][ny] ==1:
            queue.append((nx,ny))
            visit[nx][ny] = True
            result[nx][ny] = result[x][y] + 1

for i in range(n):
    for j in range(m):
        print(result[i][j],end = " ")
    print()
