# 반시계 90도 -> -1
# 후진 -> +2
dist = [(-1, 0), (0, 1), (1, 0), (0, -1)]

n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

result = 0
while True:

    if graph[x][y] == 0:
        graph[x][y] = 2
        result += 1

    flag = False
    for dx, dy in dist:
        next_x, next_y = dx + x, dy + y
        if 0 <= next_x < n and 0 <= next_y < m and not graph[next_x][next_y]:
            flag = True
            break
    if flag:
        d = (d - 1) % 4
        next_x, next_y = x + dist[d][0], y + dist[d][1]
        if 0 <= next_x < n and 0 <= next_y < m and not graph[next_x][next_y]:
            x, y = next_x, next_y
    else:
        next = (d + 2) % 4
        next_x, next_y = dist[next][0] + x, dist[next][1] + y
        if 0 <= next_x < n and 0 <= next_y < m and graph[next_x][next_y] != 1:
            x, y = next_x, next_y
        else:
            break
print(result)
