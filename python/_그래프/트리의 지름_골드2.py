v = int(input())
graph = [[] for _ in range(v + 1)]

for _ in range(v):
    info = list(map(int, input().split()))
    for i in range(1, len(info) - 1, 2):
        graph[info[0]].append((info[i], info[i + 1]))


def dfs(root):
    visited = [-1 for _ in range(v + 1)]
    stack = [root]
    visited[root] = 0
    max_node = root
    while stack:
        current = stack.pop()
        for d, w in graph[current]:
            if visited[d] == -1:
                visited[d] = visited[current] + w
                stack.append(d)

                if visited[d] > visited[max_node]:
                    max_node = d
    return max_node, visited[max_node]


long_node, long_node_result = dfs(1)

long_node, long_node_result = dfs(long_node)
print(long_node_result)
