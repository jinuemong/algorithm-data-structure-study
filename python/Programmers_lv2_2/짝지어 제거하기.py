
# 짝지어 제거하기

# 문자열 길이 : 1,000,000
# 모든 문자열 제거 가능 : 1
# 불가능 : 0
# stack에 차례대로 넣기
# -1과 현재 문자열이 같다면 pop

def solution(s):
    answer,back_stack = 0,[]
    for i in range(len(s)):
        if len(back_stack)>0 and back_stack[-1]==s[i]:
            back_stack.pop()
        else:
            back_stack.append(s[i])

    if len(back_stack)==0:
        return 1
    return answer

print(solution("cdcd"))