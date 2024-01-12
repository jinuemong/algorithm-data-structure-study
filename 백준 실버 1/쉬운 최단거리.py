
## 쉬운 최단 거리
# 모든 이동 경로 탐색

## 각 지점으로 이동거리 저장


n,m = map(int,input().split())
start = []
nm = []
for i in range(n):
    nm.append(list(map(int,input().split())))
    for j,data in enumerate(nm[-1]):
        if data == 2:
            start = [i,j]
result = [[0]*m for i in range(n)]

def dfs(current,count):
    nm[current[0]][current[1]] = 0
    result[current[0]][current[1]] = count
    if current[1]+1 < m and nm[current[0]][current[1]+1] == 1:
        dfs([current[0],current[1]+1],count + 1)
    if current[1]-1 > 1 and nm[current[0]][current[1]-1] == 1:
        dfs([current[0],current[1]-1],count + 1)
    if current[0]+1 < n and nm[current[0]+1][current[1]] == 1:
        dfs([current[0]+1,current[1]],count + 1 )
    if current[0]-1 > 1 and nm[current[0]-1][current[1]] == 1:
        dfs([current[0]-1,current[1]],count + 1 )
dfs(start,0)

for i in range(n):
    for j in range(m):
        print(result[i][j],end=" ")
    print()
