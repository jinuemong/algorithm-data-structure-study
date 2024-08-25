

# 무인도 여행
def solution(maps):
    answer = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if not visited[i][j] and maps[i][j]!="X":
                answer.append(check(visited,maps,i,j))
    if len(answer)==0: return [-1]
    return sorted(answer)

def check(visited,maps,i,j):
    visited[i][j] = True
    sum_data = int(maps[i][j])
    for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
        x,y = i+dx,j+dy
        if 0 <= x < len(maps) and 0 <= y < len(maps[0]) and maps[x][y]!="X" and not visited[x][y]:
            sum_data+=check(visited,maps,x,y)
    return sum_data


print(solution(["X591X","X1X5X","X231X", "1XXX1"]))