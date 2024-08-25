
from collections import deque
def solution(s):
    answer = 0
    s = deque(list(s))
    for _ in range(len(s)):
        data_dic = {"}":0,"]":0,")":0}
        s.append(s.popleft())
        isTrue = True
        for data in s:
            if data == "{":
                data_dic["}"]+=1
            elif data == "[":
                data_dic["]"]+=1
            elif data == "(":
                data_dic[")"]+=1
            else:
                if data_dic[data] == 0:
                    isTrue = False
                    break
                data_dic[data]-=1
        if data_dic["}"] != 0 or data_dic["]"] != 0 or data_dic[")"] != 0:
            isTrue = False
        if isTrue:
            answer+=1
    return answer

print(solution("[](){}"))