


# 위상정렬 활용
# 목표 정점의 진입 차수가 0이 되면 그 비용을 출력

import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().rstrip().split())
    d = list(map(int, sys.stdin.readline().rstrip().split())) # 소모 값 리스트
    graph = [[] for _ in range(n + 1)] # 그래프
    inDegree = [0 for _ in range(n + 1)] # 진입차수
    dp = [0 for _ in range(n + 1)] # 각 소모 값 -> 지점의 거리
    queue = deque()

    # 진입 리스트 생성 그래프에 앞으로 갈 곳 추가
    # 갈 곳에는 진입 차수 추가
    for i in range(k):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append(b)
        inDegree[b] += 1

    w = int(sys.stdin.readline().rstrip()) # 목적지

    for i in range(1, n + 1): # 각 진입차수 탐색
        if inDegree[i] == 0: # 진입차수가 0인 지점을 큐에 추가
            queue.append(i)
            dp[i] = d[i - 1] # 각 지점의 거리를 초기화

    while queue: # 큐가 비면 끝
        tmp = queue.popleft() # 큐의 제일 왼쪽 (들어온 순서로 출력 )

        for i in graph[tmp]:
            inDegree[i] -= 1  # 진입차수 -1
            dp[i] = max(dp[i], dp[tmp] + d[i - 1]) # 각 소모값의 최대값 저장
            # i -1 : 인덱스 맞추기
            if inDegree[i] == 0: # 진입차수가 0이면 큐에 추가
                queue.append(i)

    print(dp[w]) #최종적으로 목적지의 소모값 출력