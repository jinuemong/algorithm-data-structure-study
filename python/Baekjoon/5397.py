#출처 : https://www.acmicpc.net/problem/5397

t = int(input())

for _ in range(t):
    com = list(input())
    answer,answer_index= [], 0
    for c in com:
        if c=="<":
            if answer_index>0:
                answer_index-=1
        elif c==">":
            if answer_index<len(answer):
                answer_index+=1
        elif c=="-":
            if answer_index>0:
                answer_index-=1
                answer.pop(answer_index)
        else:
            answer.insert(answer_index,c)
            answer_index+=1

    print("".join(answer))