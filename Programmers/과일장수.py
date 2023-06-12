

# 과일 장수
# 한 상자에 m 개씩 담아 포장
# 가장 낮은 점수인 p 경우 상자의 가격은 p*M
# 상자 단위로 포장하며, 남은 상자는 버림
# 큰 수 부터 하나씩 넣고, 가장 작은 수가 맨 앞에 오도록
#
from  collections import deque

def solution(k, m, score):
    box_count = int(len(score)/m)
    list_que = [[] * box_count]
    i = 0
    for apple in score:

        if len(list_que[i%box_count]) >0 and list_que[i%box_count][0]>apple:
            list_que[i%box_count].insert(0,apple)
        else:
            list_que[i%box_count].append(apple)
        if len(list_que[i%box_count])==m:
            list_que[i%box_count].pop()
        i += 1

    answer = 0
    for data in list_que:
        answer+= data[0]*len(data)
    print(box_count,list_que)
    return answer

k = 3
m	= 4
score = [1, 2, 3, 1, 2, 3, 1]
print(solution(k,m,score))
