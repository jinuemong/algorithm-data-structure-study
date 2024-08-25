

# 가장 가까운 같은 글자
# 앞의 가까운 글자의 인덱스 찾기

def solution(s):
    answer = []
    data_set = {}
    for s_i in range(len(s)):
        if s[s_i] in data_set:
            answer.append(s_i - data_set[s[s_i]])
        else:
            answer.append(-1)
        data_set[s[s_i]] = s_i
    return answer


s= "banana"
print(solution(s))