

# 메뉴 리뉴얼
# 이전에 손님들이 주문을 할 때
# 가장 많이 함께 주문한 단품메뉴로 구성하려 한다.
# 최소 2명 이상의 손님으로 부터 주문 된 단품메뉴 조합에 대해서만
# 코스요리 메뉴 후보에 포함


# 문제 해석
# 단품 조합 : 최소 2개
# 문자열은 대문자, 중복 x
# 모든 손님의 단품 조합 카운트
# 생성 된 조합 많은 순으로 출력
# 원소에 저장 된 문자열은 오름차순으로 정렬 되어야 함

from itertools import combinations
def solution(orders, course):
    answer = []
    course_len = [0]*11
    orders = sorted(orders,key= lambda x : len(x))
    data_list = {}
    for order in orders:
        for cor in course:
            for value in combinations(order,cor):
                data = "".join(sorted(value))
                if data in data_list:
                    data_list[data]+=1
                    if data_list[data] > course_len[cor]:
                        course_len[cor]  = data_list[data]
                else:
                    data_list[data]=1
    for key,value in data_list.items():
        if course_len[len(key)] == value:
            answer.append(key)
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))