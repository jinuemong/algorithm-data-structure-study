

# 게임 맵 최단 거리
# 출발 :  0,0
# 도착 :  len(maps)-1 , len(maps[0])-1

d_set , answer, destination = {},-1, (0,0)
def solution(maps):
    global  d_set,answer,destination
    destination,answer = (len(maps)-1 , len(maps[0])-1), len(maps)*len(maps)
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]

    for j in range(len(maps)):
        for i in range(len(maps[0])):
            if maps[j][i]==0:
                continue
            d_list =set()
            if j -1 >=0  and maps[j-1][i]!=0:
                d_list.add((j-1,i))
            if i-1 >= 0 and maps[j][i-1]!=0:
                d_list.add((j,i-1))
            if i+1 <len(maps[0]) and maps[j][i+1]!=0:
                d_list.add((j,i+1))
            if j+1 < len(maps) and maps[j+1][i]!=0:
                d_list.add((j+1,i))
            d_set[(j,i)] = d_list
    visited[0][0]= True
    dfs(visited,1,d_set[(0,0)])
    if answer ==  len(maps)*len(maps):
        return  -1
    else:
        return answer

def dfs(visited, result,next_set):
    global d_set, answer, destination
    if len(next_set) == 0:
        return
    for next in next_set:
        if destination == next:
            if result+1 < answer:
                answer = result+1
            return
        if not visited[next[0]][next[1]]:
            visited[next[0]][next[1]] = True
            dfs(visited,result+1,d_set[next])
            visited[next[0]][next[1]] = False


maps =[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))