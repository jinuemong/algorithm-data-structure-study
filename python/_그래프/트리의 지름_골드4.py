# n = int(input())
# graph = [[] for i in range(n + 1)]
# leaf_node = []
# for _ in range(n - 1):
#     x, y, w = map(int, input().split())
#     graph[x].append((y, w))
#     graph[y].append((x, w))
#
# # 모든 leaf_node 추가
# for g in range(1, n + 1):
#     if len(graph[g]) == 1:
#         leaf_node.append(g)
#
# result = []
#
# # Leaf까지 거리 계산 함수
# def dfs(root, next_nodes):
#     visited = [-1 for _ in range(n + 1)]
#     stack = [root]
#     visited[root] = 0
#
#     while stack:
#         current = stack.pop()
#         if current in next_nodes:
#             result.append(visited[current])
#             continue
#         for d, w in graph[current]:
#             if visited[d] == -1:
#                 visited[d] = visited[current] + w
#                 stack.append(d)
#
# for i in range(len(leaf_node)):
#     dfs(leaf_node[i],set(leaf_node[i+1:]))
# print(max(result))

from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    x, y, w = map(int, input().split())
    graph[x].append((y, w))
    graph[y].append((x, w))

def bfs(start):
    visited = [-1] * (n + 1)
    q = deque([start])
    visited[start] = 0
    farthest_node = start
    max_distance = 0

    while q:
        current = q.popleft()
        for next_node, weight in graph[current]:
            if visited[next_node] == -1:  # 방문하지 않은 노드
                visited[next_node] = visited[current] + weight
                q.append(next_node)
                if visited[next_node] > max_distance:
                    max_distance = visited[next_node]
                    farthest_node = next_node

    return farthest_node, max_distance

# 1. 임의의 노드 (1번)에서 가장 먼 노드를 찾음
# 가장 먼 노드에서는 어디로 가든 가장 멈
farthest_node_from_start, _ = bfs(1)

# 2. 그 노드에서 가장 먼 노드까지의 거리를 구함 (트리의 지름)
_, max_distance = bfs(farthest_node_from_start)

# 트리의 지름 출력
print(max_distance)