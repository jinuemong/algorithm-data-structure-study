import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
n, r, q = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

v = [0]*(n+1)
query = [int(input()) for _ in range(q)]

def dfs(root):
    v[root] = 1
    for i in graph[root]:
        if not v[i]: # == 0
            dfs(i)
            v[root]+=v[i] # 현재까지의 정점을 더함
dfs(r)
for i in query:
    print(v[i])