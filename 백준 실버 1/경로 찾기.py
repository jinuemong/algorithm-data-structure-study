
n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

def dfs(x,visited):
    for i in range(n):
        if graph[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i,visited)
visited = [0 for _ in range(n)]
for i in range(n):
    dfs(i,visited)
    for j in range(n):
        if visited[j]  == 1:
            print(1,end = " ")
        else:
            print(0, end = " ")
    print()
    visited = [0 for _ in range(n)]