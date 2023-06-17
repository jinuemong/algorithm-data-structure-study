

# 의상 2
# 하나로 할 수 있는 조합 모으기
# 해당 값 삭제
# set에 더 이상 없을 때 까지 반복

def solution(clothes):
    answer = 0
    data_set = {}
    for clothe , type in clothes:
        if type in data_set:
            data_set[type].append(clothe)
        else:
            data_set[type] = [clothe]

    for data in data_set.values():
        answer*=len(data)
    if answer == len(clothes):
        return answer
    else:
        return answer+len(clothes)


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))