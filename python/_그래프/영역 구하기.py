from collections import deque
m, n, k = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j] = -1
result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] !=0:
            continue
        queue = deque([(i,j)])
        graph[i][j] = 1
        count = 1
        while queue:
            x,y = queue.popleft()
            for a,b in [(-1,0),(1,0),(0,1),(0,-1)]:
                dx,dy = x+a,y+b
                if 0<=dx<m and 0 <=dy<n and graph[dx][dy] == 0:
                    count +=1
                    graph[dx][dy] = 1
                    queue.append((dx,dy))
        result.append(count)

print(len(result))
for i in sorted(result):
    print(i,end = " ")