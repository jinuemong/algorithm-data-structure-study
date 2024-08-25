# import sys
# input = sys.stdin.readline
# direction = [(0,1),(0,-1),(1,0),(-1,0)]
# m,n = map(int,input().split())
# stack = []
# count = 0
# visited = [[] for _ in range(n)]
# for i in range(n):
#     tomato_list = list(map(int,input().split()))
#     for j, tomato in enumerate(tomato_list):
#         if tomato == 1:
#             stack.append((i,j))
#             count+=1
#         elif tomato == -1: # 비어있다면 이미 변한걸로 간주
#             count+=1
#     visited[i] = tomato_list
# result = 0
# while stack:
#     result += 1
#     next_stack = []
#     for i,j in stack:
#         for dy,dx in direction:
#             x,y = dx+j,dy+i
#             if n > y >= 0 == visited[y][x] and 0 <= x < m:
#                 count +=1
#                 visited[y][x] = 1
#                 next_stack.append((y, x))
#     stack = next_stack
#
# if count == m*n:
#     print(result-1)
# else:
#     print(-1)

m, n, h = map(int, input().split())
dist = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
stack = []
graph = [[[] for i in range(n)] for _ in range(h)]
total_count = 0
for i in range(h):
    for j in range(n):
        tomato = list(map(int, input().split()))
        for k in range(len(tomato)):
            if tomato[k] == 0:
                total_count +=1
            elif tomato[k] == 1:
                visited[i][j][k] = 1
                stack.append((i, j, k))
        graph[i][j] = tomato
result = 0
while stack:
    result += 1
    new_stack = []
    for a, b, c in stack:
        for x, y, z in dist:
            i, j, k = a + x, b + y, c + z
            if 0 <= i < h and 0 <= j < n and 0 <= k < m and not visited[i][j][k] and graph[i][j][k] != -1:
                total_count -= 1
                graph[i][j][k] = 1
                visited[i][j][k] = 1
                new_stack.append((i, j, k))
    stack = new_stack
if total_count == 0:
    print(result - 1)
else:
    print(-1)
