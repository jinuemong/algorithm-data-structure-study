
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

dp[0][graph[0][0]] = 1
dp[graph[0][0]][0] = 1

for i in range(n):
    for j in range(n):
        current = graph[i][j]
        if not dp[i][j]:
            continue
        if i == n-1 and j == n-1:
            continue
        if current+i < n:
            dp[current+i][j]+= dp[i][j]
        if current+j < n:
            dp[i][current+j]+= dp[i][j]

print(dp[n-1][n-1])