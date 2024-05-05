# union - find 활용
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


for _ in range(m):
    o, a, b = map(int, input().split())
    if o == 0:
        union(a, b)
    elif o == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
