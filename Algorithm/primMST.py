#  Prim MST 알고리즘

from math import inf
def prim(start):
    global n, adj_mat
    # 현재 방문한 정점들의 집합
    visited_set = set()
    visited_set.add(start)
    distance = 0

    # n-1 개의 간선을 선택할 때까지 반복
    for _ in range(n - 1):
        # min Dist : 현재 방문한 정점에서 갈 수 있는 간선의 최단 거리
        # next Node : 현재 방문한 정점에서 최단 거리로 갈 수 있는 정점
        min_dist, next_node = inf, -1

        # 방문한 모든 정점 확ㅇ니
        for node in visited_set:
            # 해당 정점과 연결되어 있고 아직 방문하지 않은 정점 중 소모 비용이 적은 정점 탐색
            for j in range(1, n + 1):
                if j not in visited_set and 0 < adj_mat[node][j] < min_dist:
                    min_dist = adj_mat[node][j]
                    next_node = j
        distance += min_dist
        visited_set.add(next_node)

    return distance

n,m = map(int, input().split())
adj_mat = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    x, y, value = map(int, input().split())
    adj_mat[x][y] = value
    adj_mat[y][x] = value
print(prim(1))