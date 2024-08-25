
# 햄버거 만들기
# 1: 빵, 2 : 야채 3 : 고기
# 빵 - 야채 - 고기 -빵  (1231) -> 햄버거 하나
# 문제 이해 못함 -> 순서대로 쌓을 수 있어야 한다

def solution(ingredient):
    data_set = {1 : 0 ,2: 0, 3: 0}
    for i in ingredient:
        data_set[i]+=1
    data_set[1]=int(data_set[1]/2)
    print(data_set)
    return min(data_set.values())


ingredient =[1, 3, 2, 1, 2, 1, 3, 1, 2]
print(solution(ingredient))