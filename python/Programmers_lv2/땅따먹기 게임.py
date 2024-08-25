

# 땅따먹기 게임
def solution(land):
    for i in range(1,len(land)):
        for j in range(len(land[0])):
            # 이전 방문 인덱스 제거, 이전 값에 각 행의 제일 큰 값 더하기
            land[i][j] += max(land[i-1][:j]+land[i-1][j+1:])
    return max(land[len(land)-1]) # 마지막 줄에 모인 값 중 가장 큰 값 출력


land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))