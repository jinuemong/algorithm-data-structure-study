

# 다른 섬을 거치는 경우를 고려 안함
# 반복적으로 중량을 설정하며, 이동이 가능한 경우를 찾음

# bfs를 사용해야함 (최소탐색)

from collections import deque

n, m = map(int,input().split())
adj= [[] for _ in range(n+1)]


def bfs(c): #경로 탐색 알고리즘
    # c: 중량, 다리의 가중치 weight가 중량보다 크거나 같아야 옮길 수 있음
    queue = deque([start_node])
    visited = [False]*(n+1)
    visited[start_node] = True # 첫 방문

    while queue:
        x = queue.popleft()
        for y, weight in adj[x]:
            if not visited[y] and weight >= c:
                visited[y] = True
                queue.append(y)
    return visited[end_node]

start = 1000000000
end = 1

for _ in range(m):
    x,y,weight = map(int,input().split())
    adj[x].append([y,weight])
    adj[y].append([x,weight])
    start = min(start,weight)
    end = max(end,weight)
# start에서 end로 갈 수 있는지 검사

# 공장이 존재하는 노드
start_node, end_node = map(int,input().split())

result = start # 최대 가중치를 우선 start로 설정
# 각 수를 입력받으면서 min,max을 확인하며, start,end를 갱신해줌
# start에는 가중치가 가장 작은 값
# end에는 가중치가 가장 큰 값이 저장됨
while start <= end:
    mid = (start+end)//2
    if bfs(mid): # 값을 찾을 경우 결과 갱신 (이동 가능)
        result = mid
        start = mid +1
    else: # 값이 없을 경우 중량 감소 (이동 불가능)
        end = mid -1

# start node -> end node로 가중치가 작은 값부터 탐색을 진행하므로
# 값 비교없이 최종적으로 출력 값은 최대 값이 됨
print(result)