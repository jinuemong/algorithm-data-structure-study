

# 둘만의 암호 2

def solution(s, skip, index):
    answer = ''
    answer_list = []
    for i in range(ord('a'),ord('z')+1):
        answer_list.append(chr(i))
    answer  = answer.join(answer_list)

    for i in skip:
        if i in answer:
            answer = answer.replace(i,"") # 스킵 없애기

    answer_list= []
    for i in s:
        answer_list.append(answer[(answer.index(i)+index) %len(answer)])
        # data = answer.index(i) + index
        # if data>= len(answer):
        #     answer_list.append('a')
        # else:
        #     answer_list.append(answer[data])

    return ''.join(answer_list)

print(solution("aukks","wbqd",5))