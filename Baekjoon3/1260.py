

# 깊이 우선 탐색
from collections import deque
def DFS(graph,root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()

        if n not in visited: #방문하지 않은 경우
            visited.append(n)
            print(n,end=' ')
            # 현재 꺼낸 노드에서 방문하지 않은 부분 모두 추가
            if n in graph:
                stack+=graph[n] - set(visited)
    print()

def BFS(graph,root):
    visited = []
    queue = deque([root]) # queue 생성

    while queue:
        n = queue.popleft()
        if n not in visited: # 현재 노드는 방문하지 않은 노드
            visited.append(n)
            print(n,end=' ')
            # 현재 꺼낸 노드에서 방문하지 않은 부분 모두 추가
            if n in graph:
                queue += graph[n] - set(visited)
    return visited

graph = {}
n, m, v = map(int,input().split())

for i in range(m):
    x, y = map(int,input().split())
    if x not in graph:
        graph[x] = [y]
    else:
        graph[x].append(y)

for key,data in graph.items():
    graph[key] = set(data)
print(graph)
DFS(graph,v)
BFS(graph,v)
