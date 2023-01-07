# https://www.acmicpc.net/problem/20040

n, m = map(int, input().split())

# 0 ~ n-1까지로 초기화
parent = [0] * n
for i in range(n):
    parent[i] = i


def find(x):
    if x != parent[x]:
        p = find(parent[x])  # 재귀
        parent[x] = p  # 최 상단 까지 감
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x < y: #더 큰 수가 최상단 노드
        parent[y] = x
    else:
        parent[x] = y


cycle = 0

for i in range(1, m + 1):
    a, b = map(int, input().split())

    if find(a) == find(b):
        cycle = i
        break
    else:
        union(a, b)

print(cycle)
