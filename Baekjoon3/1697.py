
from collections import  deque
# 숨바꼭질

# 걷기 :1초당 위치에서 +-1
# 순간이동 : 1초당 위치에서 *2

# 수빈이의 위치와 동생의 위치가 주어졌을 경우
# 가장 빠르게 도달하는 방법을 탐색

n , k = map(int,input().split())
result = 0
def BFS(graph,visited,start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        if v==k: # 도달
            print(result)
            return
        # 연결 점 찾기
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * 100001
graph = [[] for _ in range(100001)]
graph[0].append(1)
for i in range(1,100001):
    x,y,z = i-1,i+1,i*2
    graph[i].append(x,y,z)

BFS(graph,visited,n)