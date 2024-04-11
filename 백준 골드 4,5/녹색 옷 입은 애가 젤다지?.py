import sys
input = sys.stdin.readline
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n = int(input())
count = 0

while n != 0:
    count+=1
    n_list = [list(map(int,input().split()))for _ in range(n)]
    visited = [[float("inf")]*n for i in range(n)]
    visited[0][0] = n_list[0][0]
    def find(i,j):
        for dx, dy in direction:
            x, y = i + dx, j + dy
            if 0 <= x < n and 0 <= y < n and visited[x][y] > visited[i][j] + n_list[x][y]:
                visited[x][y] = visited[i][j] + n_list[x][y]
                find(x,y)
    find(0,0)
    print("Problem " + str(count) + ": " + str(visited[n-1][n-1]))
    n = int(input())