

# 유기농 배추
# 플러드 필 알고리즘 사용 Or 연결리스트
# 최소 배추 벌레 수 구하기
# 상하좌우 이동 가능

import sys
input = sys.stdin.readline
t = int(input().strip())
sys.setrecursionlimit(10**6)
def check(visited,i,j,farm,m,n):
    visited[i][j] = True
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x,y = i+dx,j+dy
        if 0 <= x < n and 0 <= y < m and farm[x][y] and not visited[x][y]:
            check(visited, x, y, farm, m, n)

for _ in range(t):
    answer = 0
    m, n, k = list(map(int, input().split()))
    visited = [[False for _ in range(m)] for _ in range(n)]
    farm = [[False for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        j,i = list(map(int,input().split()))
        farm[i][j] = True
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and farm[i][j]:
                answer+=1
                check(visited,i,j,farm,m,n)
    print(answer)
