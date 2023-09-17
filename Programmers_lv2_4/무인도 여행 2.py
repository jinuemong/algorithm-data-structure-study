
# 무인도 여행 2

current_sum = 0
visited = set()
def solution(maps):
    global current_sum
    answer = []
    idx_list = {(i,j):[] for i in range(len(maps)) for j in range(len(maps[0]))}
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]!="X":
                if i > 0 and maps[i-1][j]!="X":
                    idx_list[(i,j)].append((i-1,j))
                if i < len(maps)-1 and maps[i+1][j]!="X":
                    idx_list[(i,j)].append((i+1,j))
                if j > 0 and maps[i][j-1]!="X":
                    idx_list[(i,j)].append((i,j-1))
                if j < len(maps[0])-1 and maps[i][j+1]!="X":
                    idx_list[(i,j)].append((i,j+1))
    print(idx_list)
    for data,value in idx_list.items():
        if maps[data[0]][data[1]]!="X" and data not in visited:
            current_sum = maps[data[0]][data[1]]
            visited.add(data)
            check(idx_list,value,maps)
            answer+=current_sum
    print(visited)
    return sorted(answer,reverse=True)

def check(idx_list,check_list,maps):
    global current_sum
    for check in check_list:
        print(check,end=" ")
        if check not in visited:
            visited.add(check)
            current_sum+=maps[check[0]][check[1]]
            print(idx_list[check])
    print("")
print(solution(["X591X","X1X5X","X231X", "1XXX1"]))