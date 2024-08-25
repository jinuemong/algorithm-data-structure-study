




import re
def solution(skill, skill_trees):
    data_set = "".join(list({chr(i) for i in range(ord("A"),ord("Z")+1)} - set(list(skill))))
    answer = 0
    for skill_tree in skill_trees:
        data = re.sub(r"[{0}]".format(data_set),"",skill_tree)
        if skill.find(data) == 0:
            answer+=1
    return answer

# skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
# skill = "CBD"
#
# print(solution(skill,skill_trees))
#
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])) # 2
print(solution("ABC", ["DEF"]))     # 1
print(solution("CBD", ["CAD"]))     # 0
print(solution("CBD", ["AEF", "ZJW"]))  # 2
print(solution("REA", ["REA", "POA"]))  # 1
print(solution("CBDK", ["CB", "CXYB", "BD", "AECD", "ABC", "AEX", "CDB", "CBKD", "IJCB", "LMDK"]))  # 4
print(solution("BDC", ["AAAABACA"]))    # 0
print(solution("CBD", ["C", "D", "CB", "BDA"])) # 2