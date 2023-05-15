

from collections import deque

n,m,v = map(int,input().split())
adj = [[] for _ in range(n+1)]
def dfs(v,visited):
    print(v,end= ' ')
    visited[v] = True
    for e in adj[v]: #연결점찾기
        if not(visited[e]): # 방문하지 않음
            dfs(e,visited)

def bfs(v,visiited):
    q = deque([v])
    while q:
        v = q.popleft()
        if not(visiited[v]):
            visiited[v] = True
            print(v,end=' ')
            for e in adj[v]: #연결점 찾기
                if not visiited[e]: #방문하지 않음
                    q.append(e)

for _ in range(m):
    x,y = map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)
for e in adj:
    e.sort()

visited = [False] * (n+1)
dfs(v,visited)
print()
visited = [False] * (n+1)
bfs(v,visited)