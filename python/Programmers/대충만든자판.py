
# 대충 만든 자판


def solution(keymap, targets):
    answer = []
    for target in targets:
        sum = 0
        for t in target:
            result = 101
            for key in keymap:
                data = key.find(t)
                if data!=-1 and data+1<result:
                    result = data+1
            if result!=101:
                sum+=result
            else:
                sum = -1
                break
        answer.append(sum)


    return answer


keymap = ["ABACD", "BCEFD"] # 1~ 100
targets = ["ABCD","AABB"] # 1 ~ 100
print(solution(keymap,targets))