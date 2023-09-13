

# 두 큐 합 같게 만들기

from collections import deque
def solution(queue1, queue2):
    answer = 0
    queue1, queue2 = deque(queue1), deque(queue2)
    sum_1, sum_2 = sum(queue1), sum(queue2)
    if (sum_1+sum_2)%2!=0:
        return -1
    while True:
        if answer > len(queue1)*2+len(queue2)*2: return -1
        if sum_1>sum_2:
            value = queue1.popleft()
            queue2.append(value)
            sum_2+=value
            sum_1-=value
        elif sum_1<sum_2:
            value = queue2.popleft()
            queue1.append(value)
            sum_1+=value
            sum_2-=value
        else: return answer
        answer+=1

print(solution([3, 2, 7, 2],[4, 6, 5, 1]))