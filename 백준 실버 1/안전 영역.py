
n = int(input())

graph = [list(map(int,input().split()))for _ in range(n)]

max_result = 1
count = 0
while True:
    result = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > count:
                stack = [(i,j)]
                result+=1

                while stack:
                    a,b = stack.pop()
                    visited[a][b] = 1
                    for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
                        q,r = a+x,b+y
                        if 0<=q<n and 0<=r<n and not visited[q][r] and graph[q][r] > count:
                            stack.append((q,r))

    if result ==0:
        break
    if max_result <= result:
        max_result = result
        max_result_count = count
    count+=1
print(max_result)
