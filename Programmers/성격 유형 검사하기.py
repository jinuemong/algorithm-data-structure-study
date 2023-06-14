


# 성격 유형 검사하기
# 같은 성격 유형이 나올 경우 사전 순으로 빠른 것이 성격 유형

data_set = {"R":0,"T":0, "C":0,"F":0, "J":0,"M":0, "A":0,"N":0}
def solution(survey, choices):
    answer = ''
    # answer = ['T','C','J','A']
    for i in range(len(survey)):
        if choices[i]<4:
            data_set[survey[i][0]]+=(4-choices[i])
        elif choices[i]>4:
            data_set[survey[i][1]]+=(choices[i]-4)

    li = list(data_set.items())

    for i in range(0, 8, 2):
        if li[i][1] < li[i + 1][1]:
            answer += li[i + 1][0]
        else:
            answer += li[i][0]

    return answer
    # if data_set['R'] > data_set['T']:
    #     answer[0] = 'R'
    # if data_set['F'] > data_set['C']:
    #     answer[1] = 'F'
    # if data_set['M'] > data_set['J']:
    #     answer[2] = 'M'
    # if data_set['N'] > data_set['A']:
    #     answer[3] = 'N'
    #
    # return ''.join(answer)

survey =["TR", "RT", "TR"]
choices =[7, 1, 3]
print(solution(survey,choices))