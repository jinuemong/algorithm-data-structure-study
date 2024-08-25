from queue import deque

n, l, r = map(int, input().split())

# l <= 인구 차이 <=r 국경선 염
# 열어야하는 국경선이 모두 열리면 인구 이동
# 하루 동안 연합
# 연합 끼리 초 인구수 / 연합의 개수를 나눠가지며 소수점은 버림

a = [list(map(int, input().split())) for _ in range(n)]
result = 0


def union_bfs(i, j, visited):
    queue = deque([(i, j)])
    union = [(i, j)]
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for x2, y2 in ((x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= x2 < n and 0 <= y2 < n and not visited[x2][y2]:
                if l <= abs(a[x2][y2] - a[x][y]) <= r:
                    visited[x2][y2] = 1
                    queue.append((x2, y2))
                    union.append((x2, y2))
    return union


while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                current = union_bfs(i, j, visited)

                if len(current) > 1:
                    flag = True
                    count = int(sum(a[x][y] for x, y in current) // len(current))
                    for x, y in current:
                        a[x][y] = count
    if not flag:
        print(result)
        break
    else:
        result+=1
