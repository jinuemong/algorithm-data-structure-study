# 1: X-1, X + 1
# 0: 2*X
from collections import deque

def bfs(n, k):
    visited = [0] * 100001
    q = deque([])
    q.append(n)

    while q:
        current = q.popleft()
        if current == k:
            return visited[current]

        for next in (current - 1, current + 1, current * 2):
            if 0 <= next <= 100000:
                if visited[next] == 0:
                    if next == current * 2 and next != 0:
                        visited[next] = visited[current]
                        # 더 적은 소모값을 앞으로 이동
                        q.appendleft(next)
                    else: ## *2 한 경우 -> 그대로 이동
                        visited[next] = visited[current] + 1  ## 방문했으니 + 1
                        q.append(next)

n, k = map(int, input().split())
print(bfs(n, k))
