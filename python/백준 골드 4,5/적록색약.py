n = int(input())
graph = [list(input()) for i in range(n)]


def dfs():
    visited = [[0 for _ in range(n)] for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            stack = [(i, j)]
            visited[i][j] = 1
            count = 1
            while stack:
                a, b = stack.pop()
                for x, y in ((a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1)):
                    if 0 <= x < n and 0 <= y < n and graph[x][y] == graph[a][b] and not visited[x][y]:
                        visited[x][y] = 1
                        count += 1
                        stack.append((x, y))
            result.append(count)
    return len(result)

print(dfs(),end =" ")
for i in range(n):
    for j in range(n):
        if graph[i][j] == "G":
            graph[i][j] = "R"
print(dfs())
