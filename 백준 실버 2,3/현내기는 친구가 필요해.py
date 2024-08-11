n,m = map(int,input().split())
result = 0
stack = []
graph = []
visited = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    m_list = list(input())
    for j in range(m):
        if m_list[j] == "I":
            stack.append((i,j))
    graph.append(m_list)

while stack:
    a,b = stack.pop()
    for x,y in ((a+1,b),(a-1,b),(a,b+1),(a,b-1)):
        if 0<=x<n and 0<=y<m and not visited[x][y] and graph[x][y] != "X":
            visited[x][y] = 1
            if graph[x][y] == "P":
                result+=1
            stack.append((x,y))
if result:
    print(result)
else:
    print("TT")
