import sys
input = sys.stdin.readline
direction = [(0,1),(0,-1),(1,0),(-1,0)]
m,n = map(int,input().split())
stack = []
count = 0
visited = [[] for _ in range(n)]
for i in range(n):
    tomato_list = list(map(int,input().split()))
    for j, tomato in enumerate(tomato_list):
        if tomato == 1:
            stack.append((i,j))
            count+=1
        elif tomato == -1: # 비어있다면 이미 변한걸로 간주
            count+=1
    visited[i] = tomato_list
result = 0
while stack:
    result += 1
    next_stack = []
    for i,j in stack:
        for dy,dx in direction:
            x,y = dx+j,dy+i
            if n > y >= 0 == visited[y][x] and 0 <= x < m:
                count +=1
                visited[y][x] = 1
                next_stack.append((y, x))
    stack = next_stack

if count == m*n:
    print(result-1)
else:
    print(-1)
