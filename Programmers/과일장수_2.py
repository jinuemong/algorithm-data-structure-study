# 과일 장수
# 한 상자에 m 개씩 담아 포장
# 가장 낮은 점수인 p 경우 상자의 가격은 p*M
# 상자 단위로 포장하며, 남은 상자는 버림
# 큰 수 부터 하나씩 넣고, 가장 작은 수가 맨 앞에 오도록
#
from  collections import deque

def solution(k, m, score):
    score = sorted(score, reverse=True)
    answer = 0
    for i in range(0,len(score),m):
        if i+m <=len(score):
            answer+=min(score[i:i+m])*m

    return answer

k = 3
m	= 4
score =  [1, 2, 3, 1, 2, 3, 1]
print(solution(k,m,score))