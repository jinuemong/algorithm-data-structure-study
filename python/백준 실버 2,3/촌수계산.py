n = int(input())
graph = [[] for _ in range(n+1)]
a,b = map(int,input().split())
for _ in range(int(input())):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [0] * (n+1)
result = -1
def dfs(v,num):
    global result
    visited[v] = 1

    if v == b:
        result = num

    for i in graph[v]:
        if not visited[i]:
            dfs(i,num+1)
dfs(a,0)
print(result)



