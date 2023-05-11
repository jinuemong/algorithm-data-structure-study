
# 위상 정렬

import sys
input = sys.stdin.readline
import heapq
n,m = map(int,input().split())

indegree = [0] * (n+1)
graph = [[] for _ in range(0,n+1)]

for i in range(m):
    a, b=  map(int,input().split())
    graph[a].append(b)
    indegree[b] +=1

def topology_sort():
    result = []
    heap = []
    # 초기 세팅 ->  진입차수가 0인 값 추가
    for i in range(1,n+1):
        if indegree[i] == 0:
            heapq.heappush(heap,i)

    while heap:
        current = heapq.heappop(heap)
        result.append(current)

        for i in graph[current]:
            # current로 부터 나가는 간선 제거
            indegree[i]-=1
            # 간선이 0이 되었다면 다시 추가
            if indegree[i]==0:
                heapq.heappush(heap,i)

    for i in result:
        print(i,end=" ")

topology_sort()
