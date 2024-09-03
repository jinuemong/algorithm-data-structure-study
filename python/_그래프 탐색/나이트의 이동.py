from collections import deque

dist = [(2,-1),(2,1),(1,-2),(1,2),(-2,-1),(-2,1),(-1,-2),(-1,2)]
for _ in range(int(input())):
    n = int(input())
    visited = [[0] * n for _ in range(n)]
    start_x,start_y = map(int,input().split())
    end_x,end_y = map(int,input().split())

    queue = deque([(start_x,start_y,0)])

    while queue:
        a,b,c = queue.popleft()
        if a == end_x and b == end_y:
            print(c)
            break
        for nx,ny in dist:
            x,y = nx+a,ny+b
            if 0<=x<n and 0<=y<n and not visited[x][y]:
                visited[x][y] = 1
                queue.append((x,y,c+1))
