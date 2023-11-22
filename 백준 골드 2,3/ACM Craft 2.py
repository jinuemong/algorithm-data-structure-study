

# 실패 이유 : 출발지가 아닌 도착지가 주어진다.
# 역으로 문제를 풀어야함

import sys
input = sys.stdin.readline
t = int(input())

def drf(next,depth,graph,d_stack,d_list):
    d_stack[depth] = max(d_list[next],d_stack[depth])
    for data in graph[next]:
        if data in graph:
            drf(data,depth+1,graph,d_stack,d_list)
for _ in range(t):
    n,k = list(map(int,input().split()))
    d_list = list(map(int,input().split())) # 건물 건설 시간 리스트
    d_stack = [0 for _ in range(n+1)] # 깊이 별 모음
    graph = {i:[] for i in range(0,n)}
    for _ in range(k): #그래프 생성
        x,y = list(map(int,input().split()))
        graph[y-1].append(x-1)
    root = int(input())
    drf(root-1,0,graph,d_stack,d_list)
    answer = 0
    for data in d_stack:
        answer+=data
    print(answer)
