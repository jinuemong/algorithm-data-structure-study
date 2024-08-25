

def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        if skill.find("".join([ch for ch in skill_tree if ch in skill])) == 0:
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