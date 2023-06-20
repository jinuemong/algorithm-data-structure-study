

# 의상

def solution(clothes):
    answer = 1
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