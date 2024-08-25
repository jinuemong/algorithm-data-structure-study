# 출처 : https://www.acmicpc.net/problem/4195
# 문제풀이

parent = dict()
number = dict()


def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]


def union(x, y):
    x = find(x) #최상위 합집합으로 이동
    y = find(y) #최상위 합집합으로 이동

    # 같으면 이미 합집합
    if x != y:
        parent[y] = x
        number[x] += number[y]


t = int(input())

for _ in range(t):
    parent = dict()
    number = dict()
    f = int(input())

    for _ in range(f):
        f1, f2 = input().split(' ')

        # 자기 자신 포함
        if f1 not in parent:
            parent[f1] = f1
            number[f1] = 1
        if f2 not in parent:
            parent[f2] = f2
            number[f2] = 1

        union(f1, f2)

        print(number[find(f1)])

