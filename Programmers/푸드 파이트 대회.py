

# 푸드 파이트 대회
# 왼 -> 오   물  오 <- 왼
# 공정한 대회를 위해서 음식의 종류와 양, 순서가 같아야 함
# 칼로리가 낮은 음식부터 먹어야 함


def solution(food):
    answer = ''
    for i in range(1,len(food)):
        answer+=(int(food[i]/2)*str(i))
    return answer + "0" + answer[::-1]


food = [1, 3, 4, 6]
print(solution(food))