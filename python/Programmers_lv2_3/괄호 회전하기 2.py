

# 괄호 회전하기

def bracket(s):
    stack = []
    for i in s:
        if len(stack) == 0: stack.append(i)
        else:
            if i == ")" and stack[-1] == "(": stack.pop()
            elif i == "]" and stack[-1] == "[": stack.pop()
            elif i == "}" and stack[-1] == "{": stack.pop()
            else: stack.append(i)
    return 1 if len(stack)==0 else 0

def solution(s):
    answer = 0
    for _ in range(len(s)):
        answer+=bracket(s)
        s = s[1:] + s[:1]
    return answer

print(solution("[](){}"))