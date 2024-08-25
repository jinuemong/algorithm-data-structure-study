

# 튜플

# 순서를 따르는 요소들의 모음
# n개의 요소를 가진 튜플 : n - 튜플
# a1, a2, a3 ,,,,, an
# 중복된 원소가 있을 수 있으며, 순서가 다르다면 다른 튜플
# {2,1,3,4}인 경우
# {{2},{2,1},{2,1,3},{2,1,3,4}}

#{{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}}
#{{2, 1, 3, 4}, {2}, {2, 1, 3}, {2, 1}}
#{{1, 2, 3}, {2, 1}, {1, 2, 4, 3}, {2}}

# 특정 튜블을 표현하는 집합이 담긴 문자열이 주어졌을 때, 표현하는 튜플을 배열에 담아 리턴

def solution(s):
    data_list = sorted([data.replace("{", "",).replace( "}", "").split(",") for data in s.split("},")],key=len)
    answer = [int((set(data_list[i+1]) - set(data_list[i])).pop()) for i in range(len(data_list)-1)]
    answer.insert(0,int(data_list[0][0]))
    return answer

s= "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))