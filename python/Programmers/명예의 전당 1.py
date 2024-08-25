

# 명예의 전당 레벨 1

# 일차에 따라서 점수가 부여
# 해당 점수가 명예의 전당 (k 번째 까지의 순위)
# 에 포함되면 추가
# 해당 일차의 명예의 전당은 최하위 점수 발표
# k < 100 , score < 1000

array = [] #명예의 전당

def solution(k, score):
    answer = []

    for s in score:
        if len(array) < k:
            array.append(s)
        else:
            if s >= array[0]:
                array.pop(0)
                array.append(s)
        array.sort()
        answer.append(array[0])

    return answer





k=4
score = [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]
print(solution(k,score))