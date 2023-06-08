

# 카드 뭉치
# [규칙]
# 카드는 순서대로 한 장씩
# 한 번 사용한 카드는 다시 사용할 수 없음
# 카드를 사용하지 않을 수 없음
# 카드 뭉치의 순서를 바꿀 수 없음

def solution(cards1, cards2, goal):
    answer = 'Yes'
    data_dic = {}
    data_dic[cards1.pop(0)] = "cards1"
    data_dic[cards2.pop(0)] = "cards2"

    while len(goal)>0:
        data = goal.pop(0)
        if data in data_dic:
            value = data_dic.pop(data)
            if value=="cards1" and len(cards1)>0:
                data_dic[cards1.pop(0)] = "cards1"
            elif value == "cards2" and len(cards2)>0:
                data_dic[cards2.pop(0)] = "cards2"
        else:
            return "No"
    return answer

cards1 = ["i", "water", "drink"]	 # 1~10
cards2 = ["want", "to"] # 1~ 10
goal = ["i", "want", "to", "drink", "water"] # 2~ card1+card2
print(solution(cards1,cards2,goal))