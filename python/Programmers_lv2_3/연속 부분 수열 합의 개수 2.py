

#2번 째 -> 시간초과
# deque 활용
from collections import deque
def solution(elements):
    answer = set()
    elements = deque(elements)
    for i in range(1,len(elements)+1):
        for j in range(len(elements)):
            data = 0
            for _ in range(i):
                pop_data = elements.pop()
                data+=pop_data
                elements.appendleft(pop_data)
            answer.add(data)
    return len(answer)


print(solution([7,9,1,1,4]))