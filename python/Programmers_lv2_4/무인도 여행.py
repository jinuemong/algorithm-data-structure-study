

# 무인도 여행


def solution(maps):
    answer = []
    idx_list = set()
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if (i,j) not in idx_list and maps[i][j]!="X": #탐색 시작
                print(i,j)
    return answer

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))
