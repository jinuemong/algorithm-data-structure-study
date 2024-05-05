
# 원소들의 연결 여부를 확인며 부모가 더 작은 원소를 부모로 삼도록 한다
# 여러 노드가 존재할 때, 두 개의 노드를 선택해서 현재 노드가 서로 같은 그래프에 속하는지 판별

n, m = map(int,input().split())

parent = [ [i] for i in range(n+1)]

def find(x):
    if x == parent[x]: # 자기 자신이 루트 노드면 반환
        return x
    p = find(parent[x]) # x의 루트 노드 찾기
    parent[x] = p # 부모 테이블을 갱신
    return parent[x] # x의 루트 노드 반환

# x가 속해있는 집합과 y가 속해있는 집합 합치기
def union(x,y):
    x = find(x) # x의 루트
    y = find(y) # y의 루트

    if x == y:
        return # 이미 동일한 집합
    if x < y: # 서로 루트가 다르면 주 집합 합치기
        parent[y] = x
    else:
        parent[x] = y

