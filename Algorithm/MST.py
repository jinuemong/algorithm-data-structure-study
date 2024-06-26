# Minimum Spanning Tree : 최소 신장 트리
# 사용된 간선들의 가중치 합이 최소인 트리

# 특징

# 가장 적은 간선을 사용한다고 최소 비용이 얻어지지 않는다
# 가중치를 고려하여 최소 비용으로 선택하는 것을 말한다
# 네트워크에 있는 모든 정점들을 가장 적은 수의 간선과 비용으로 연결하는 것이다

# 사용 사례

# 도로 건설, 전기 회로, 통신, 배관 등 최소의 길이로 연결하는 문제

# 구현 방법

# 그리드 알고리즘 활용
# 가중치의 모든 정점을 최소 비용으로 연결하는 최적 해답을 구함
# 아래와 같은 조건을 적용한다
# 최소 비용의 간선으로 구성됨
# 사이클을 포함하지 않음
# 이전 신장 트리와는 상관없이 무조건 최소 간선만을 선택

### Kruskal MST 알고리즘
# 1. 그래프의 간선들을 가중치의 오름차순으로 정렬
# 2. 정렬된 간선 리스트에서 순서대로 사이클을 형성하지 않는 간선을 선택
#   - 가장 낮은 가중치 선택
#   - 사이클을 형성하는 간선 제외
#   - 해당 간선을 현재의 MST의 집합에 추가
# -> 크루스칼 MST 알고리즘 활용

### Prim MST 알고리즘
# 시작 정점에서부터 출발하여 신장트리 집합을 단계적으로 확장해 나가는 방법
# 1. 정점 선택을 기반으로 하는 알고리즘
# 2. 이전 단계에서 만들어진 신장 트리를 확장
#   - 시작 단계에서는 시작 정점만이 MST 집합에 포함
#   - 앞 단계에서 만들어진 MST 집합에 인접한 정점들 중에서 최소 간선으로 연결된 정점을 선택하여 트리 확장
#   - 가장 낮은 가중치 먼저 선택
# -> Prim MST 알고리즘 활용

### 크루스칼 with 파이썬
# 모든 간선을 가중치 오름차순으로 ㅈ어렬
# 가중치가 낮은 간선부터 순회
# 이 간선이 추가된다면 사이클이 발생하는지 확인
# 사이클 발생 -> continue
# else -> 추가
# 모든 간선을 돌고 나면 추가된 간선들이 최소 신장 트리

# 사이클 확인
# union find 활용 -> Kruskal MST 알고리즘

import sys
input = sys.stdin.readline

v, e = map(int, input().split())
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
edges.sort(key=lambda x: x[2])  # 간선이 작은 순
parent = [i for i in range(v + 1)] #부모를 기준으로 union

def find(x):
    if parent[x] != x: # 자기 자신이 루트 노드가 아니라면
        parent[x] = find(parent[x]) # 부모 노드를 찾아서 갱신
    return parent[x] # 자기 자신이 루트 노드라면 그대로 반환

# x가 속해있는 집합과 y가 속해있는 집합 합치기
def union(x, y):
    x = find(x)  # x의 루트
    y = find(y)  # y의 루트

    # 서로 루트가 다르면 주 집합 합치기
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
answer = 0
for v,e,h in edges:
    if find(v) != find(e):
        union(v,e)
        answer+=h
print(answer)