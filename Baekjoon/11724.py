# https://www.acmicpc.net/problem/11724

n, m = map(int,input().split())

parent = [0]*n
for i in range(n):
    parent[i]=i

def find(x):
    if x!=parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    # 더 작은 값으로 변경
    if x<y:
        parent[y]= x
    else:
        parent[x]=y

for i in range(m):
    u,v = map(int,input().split())

    # parent가 0부터 시작하므로 맞추기
    u-=1
    v-=1
    union(u,v)

for i in range(n):
    find(i)
print(len(set(parent)))


