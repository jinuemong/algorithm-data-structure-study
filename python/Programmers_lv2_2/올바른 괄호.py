

# 올바른 괄호
# ( - ) 규칙을 만족해야 함
# 괄호가 닫히지 않는다면 올바르지 않은 괄호
# 올바른 괄호 상태라면 True 반환

def solution(s):
    data_set = {"(":0}
    for s_i in list(s):
        if s_i == "(":
            data_set[s_i]+=1
        else:
            data_set["("]-=1
            if data_set["("]<0:
                return False
    if data_set["("]!=0:
        return False
    return True

    print(data_set)


s = "(()("
print(solution(s))