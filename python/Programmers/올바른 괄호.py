def solution(s):
    data_set = {"(": 0}
    for s_i in list(s):
        if s_i == "(":
            data_set[s_i] += 1
        else:
            data_set["("] -= 1
            if data_set["("] < 0:
                return False
    if data_set["("] != 0:
        return False
    return True
