import sys

input = sys.stdin.readline

V, E = map(int, input().split())

edges = []

for _ in range(E):
    v, e, h = map(int, input().split())
    edges.append((v, e, h))
edges.sort(key=lambda x: x[2])

parent = [i for i in range(V + 1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y
ansewr = 0
for v,e,h in edges:
    if find(v) != find(e):
        union(v,e)
        ansewr+=h
print(ansewr)

