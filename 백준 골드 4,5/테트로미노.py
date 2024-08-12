n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dist = [(0, 1), (0, -1), (1, 0), (-1, 0)]

maximum = 0
visited = [[0 for _ in range(m)] for _ in range(n)]

def dfs(i, j,step,total):
    global maximum,visited

    if step == 4:
        maximum = max(maximum,total)
        return

    for x, y in dist:
        nx,ny =  x+i,y+j
        if 0<= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx,ny,step+1,total+graph[nx][ny])
            visited[nx][ny] = False
def fuck(a,b):
    global maximum
    arr = []
    for x,y in dist:
        nx,ny = x+a,y+b
        if 0<=nx < n and 0 <= ny < m:
            arr.append(graph[nx][ny])
    if len(arr) == 4:
        maximum = max(maximum, sum(arr) - min(arr) + graph[a][b])
    elif len(arr) == 3:
        maximum = max(maximum, sum(arr) + graph[a][b])
    return

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,1,graph[i][j])
        visited[i][j] = False
        fuck(i,j)
print(maximum)