
n,m = map(int,input().split())
result = [0]
graph = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j]:
            count = 1
            stack = [(i,j)]
            graph[i][j] = 0

            while stack:
                x,y = stack.pop()
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    next_x,next_y = x+dx, y+dy
                    if 0<=next_x<n and 0<=next_y<m and graph[next_x][next_y]:
                        stack.append((next_x,next_y))
                        graph[next_x][next_y] = 0
                        count += 1
            result.append(count)
print(len(result)-1)
print(max(result))