
# 2개의 마을로 분리
# 각 집은 두 집 사이의 경로가 항상 존재하는 집들의 집합

n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(m)]
graph.sort(key = lambda x : x[2])

parent = [i for i in range(n+1)]

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
max_value = 0
answer = 0
for v,e,h in graph:
    if find(v) != find(e):
        union(v,e)
        answer+=h
        if max_value < h :
            max_value = h
print(answer- max_value )