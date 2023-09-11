
# 3번째
from collections import deque
def solution(elements):
    answer = set()
    for i in range(0,len(elements)):
        element_que = deque(elements[i:]+elements[:i])
        data = 0
        for _ in range(len(elements)):
            element_que_data = element_que.pop()
            data+=element_que_data
            answer.add(data)
            element_que.appendleft(element_que_data)
    return len(answer)


print(solution([7,9,1,1,4]))