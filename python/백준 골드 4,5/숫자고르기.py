
n = int(input())
graph = [[]for i in range(n+1)]

visited = [False for i in range(n+1)]
result = []

def dfs(v, i):
    visited[v] = True
    for k in graph[v]:
        if not visited[k]:
            dfs(k,i)
        elif visited[k] and k == i :
            result.append(k)

for i in range(1,n+1):
    graph[int(input())].append(i)

for i in range(1,n+1):
    visited = [False for i in range(n + 1)]
    dfs(i,i)

print(len(result))
for i in result:
    print(i)