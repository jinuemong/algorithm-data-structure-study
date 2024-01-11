
# 제일 위 카드 버리기
# 제일 위 카드를 제일 아래로 이동
# 가장 마지막에 남은 카드 리턴

from collections  import deque

que = deque([i+1 for i in range(int(input()))])

while len(que) > 1:
    que.popleft()
    que.append(que.popleft())
print(que[0])

