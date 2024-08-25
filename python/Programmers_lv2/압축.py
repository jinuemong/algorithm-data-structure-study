

# 압축

# 전송 효율을 높이기 위한 압축

def solution(msg):
    answer = []
    msg = list(msg) + ["0"]
    di = {a : i+1 for i,a in enumerate([chr(i) for i in range(ord("A"),ord("Z")+1)])}
    start,end = 0,1
    while end < len(msg):
        while ''.join(msg[start:end]) in di:
            end+=1 # 사전에 없는 단어 발견할 때까지 +1
        di[''.join(msg[start:end])] = len(di)+1
        answer.append(di[''.join(msg[start:end-1])])

        start , end = end -1, end
    return answer

msg = "ABABABABABABABAB"
print(solution(msg))