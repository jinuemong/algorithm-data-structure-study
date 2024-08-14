# from collections import deque
# # 가장 오래 걸리는 법 -> +로 도착 or -로 도착 : abs(n-k)
# n, k = map(int, input().split())
# maximum = abs(n-k)
#
# result = []
# visited = [-1] * 100001
# graph = deque([(0,n)])
#
# while graph:
#     v,c = graph.popleft()
#     if v > maximum or c >= maximum*2+1 or c < 0:
#         continue
#     if c == k:
#         if len(result)==0 or result[0]==v:
#             result.append(v)
#     graph.append((v+1, c * 2))
#     graph.append((v+1, c - 1))
#     graph.append((v+1, c + 1))
#
# print(result[0])
# print(len(result))

from collections import deque

n, k = map(int, input().split())

visited = [-1] * 100001
visited[n] = 0

queue = deque([n])
ways = 0

while queue:
    current = queue.popleft()
    if current == k:
        ways += 1
        continue
    for next_pos in (current - 1, current + 1, current * 2):
        if 0 <= next_pos <= 100000:
            if visited[next_pos] == -1 or visited[next_pos] == visited[current] + 1:
                visited[next_pos] = visited[current] + 1
                queue.append(next_pos)

print(visited[k])
print(ways)