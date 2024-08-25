r, c = map(int, input().split())

sheep, woof = 0, 0
graph = []
visited = [[0 for _ in range(c)] for _ in range(r)]
for _ in range(r):
    shape = list(input())
    sheep += shape.count("o")
    woof += shape.count("v")
    graph.append(shape)
for i in range(r):
    for j in range(c):
        if not visited[i][j] and graph[i][j] != "#":
            stack = [(i, j)]
            sheep_num, woof_num = 0, 0
            while stack:
                a, b = stack.pop()
                if visited[a][b]:
                    continue
                if graph[a][b] == "v":
                    woof_num += 1
                if graph[a][b] == "o":
                    sheep_num += 1
                visited[a][b] = 1
                for ax,ay in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    x, y = a + ax, b + ay
                    if 0 <= x < r and 0 <= y < c and not visited[x][y] and graph[x][y] != "#":
                        stack.append((x, y))
            if sheep_num > woof_num:
                woof -= woof_num
            else:
                sheep -= sheep_num
print(sheep, woof)
