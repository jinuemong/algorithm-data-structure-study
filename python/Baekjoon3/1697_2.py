

from collections import deque

max =100001
n,k = map(int,input().split())
array  = [0]* max

def bfs():
    q = deque([n])
    while q:
        now = q.popleft()
        if now == k:
            return array[now]
        for next in (now -1 , now + 1, now * 2 ):
            if 0 <= next < max and not array[next]:
                # 수의 범위이고, 방문하지 않았을 때
                array[next] = array[now] + 1 # 이전 가지 +1
                q.append(next) # 다음으로 방문
print(bfs())