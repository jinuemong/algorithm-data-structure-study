

# 삼각 달팽이
# 정수 n이 매개변수로 주어질 때
# 밑변의 길이와 높이가 n인 삼각형에서
# 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기 진행

def solution(n):
    dicts = [[1,0],[0,1],[-1,-1]]
    answer,current , count= [[0]*n for _ in range(n)], [-1,0], 1

    for i in range(n):
        for j in range(n-i):
            current[0]+=dicts[i%3][0]
            current[1]+=dicts[i%3][1]
            answer[current[0]][current[1]] = count
            count+=1
    return [answer[i][j] for i in range(n) for j in range(n) if answer[i][j]!=0]

print(solution(5))