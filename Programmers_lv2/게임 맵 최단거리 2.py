
# 게임 맵 최단 거리
# 출발 :  0,0
# 도착 :  len(maps)-1 , len(maps[0])-1

import math
answer, destination = -1, (0 ,0)
def solution(maps):
    global answer ,destination
    destination = (len(maps ) -1 , len(maps[0] ) -1)
    visited = [[False ] *len(maps[0]) for _ in range(len(maps))]
    visited[0][0] = True
    dfs(visited ,1 ,(0 ,0) ,maps)
    return answer

def dfs(visited, result ,data ,maps):
    global answer, destination
    if result > answer != -1:
        return
    j ,i ,next_set =data[0], data[1], set()

    if j - 1 >= 0 and maps[j - 1][i] != 0 and not visited[j - 1][i]:
        next_set.add((j - 1, i,math.sqrt()))
    if i - 1 >= 0 and maps[j][i - 1] != 0 and not visited[j][i - 1]:
        next_set.add((j, i - 1))
    if i + 1 < len(maps[0]) and maps[j][i + 1] != 0 and not visited[j][i + 1]:
        next_set.add((j, i + 1))
    if j + 1 < len(maps) and maps[j + 1][i] != 0 and not visited[j + 1][i]:
        next_set.add((j + 1, i))

    for next in next_set:
        if destination == next:
            if result + 1 < answer or answer == -1:
                answer = result + 1
            return
        visited[next[0]][next[1]] = True
        dfs(visited, result + 1, next, maps)
        visited[next[0]][next[1]] = False


maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
print(solution(maps))
