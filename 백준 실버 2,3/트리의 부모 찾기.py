import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for i in range(N+1)]
result = [0]*(N+1)
for _ in range(N-1):
    n,v = map(int,input().split())
    graph[n].append(v)
    graph[v].append(n)
def dfs(current):
    for i in graph[current]:
        if result[i] == 0:
            result[i] = current
            dfs(i)
dfs(1)
for i in range(2,N+1):
    print(result[i])

from collections import deque
queue = deque()
queue.append(1)
def bfs():
    while queue:
        current = queue.popleft()
        for next in graph[current]:
            if result[next] == 0:
                result[next] = current
                queue.append(next)
bfs()
for i in range(2,N+1):
    print(result[i])