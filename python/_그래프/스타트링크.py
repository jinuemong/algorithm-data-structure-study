# 0 ~ F
# U : + U
# D : - D
# S : my
# G : next

from collections import deque
F, S, G, U, D = map(int,input().split())

visited = [-1]*(F+1)
visited[S] = 0
queue = deque([S])
while queue:
    current= queue.popleft()
    if current == G:
        break
    for i in [current+U, current-D]:
        if 0<i<=F and visited[i]==-1:
            visited[i] = visited[current]+1
            queue.append(i)

if visited[G] == -1:
    print("use the stairs")
else:
    print(visited[G])