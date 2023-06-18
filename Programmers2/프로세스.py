

# 프로세스

# 규칙
# 실행 대기 큐에서 대기중인 프로세스 꺼냄
# 큐에 대기 중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣음
# 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스 실행
# 한 번 실행한 프로세스는 종료

from collections import deque
def solution(priorities, location):
    queue = deque([[p, i] for i, p in enumerate(priorities)])
    for idx,current in enumerate(sorted(priorities,reverse=True)):
        while queue:
            data = queue.popleft()
            if data[0] == current:
                if location == data[1]:
                    return idx + 1
                break
            else:
                queue.append(data)
    return


priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities,location))