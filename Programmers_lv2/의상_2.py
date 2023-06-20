

# 의상 2
# 하나로 할 수 있는 조합 모으기
# 갈 수 있는 길 찾기
# 첫 원소에서 출발
# 재귀 함수를 통해서 계속 이동
# 마지막 지점 도착 시 1 반환

def solution(clothes):
    answer = 1
    data_set = {}
    for clothe , type in clothes:
        if type in data_set:
            data_set[type].add(clothe)
        else:
            data_set[type] = {clothe}

    for value in data_set.values():
        answer*=(len(value)+1) #입지 않은 경우 추가 
    return answer -1 # 아무것도 입지 않는 경우 제외


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))