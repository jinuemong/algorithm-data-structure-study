

# ACM Craft.py
import sys
input = sys.stdin.readline
t = int(input())

def check(stack,depth,graph,d_stack,d_list,visited):
    for data in stack:
        d_stack[depth].append(d_list[data-1])
        visited.add(data)
        if data in graph and data not in visited:
            check(graph[data],depth+1,graph,d_stack,d_list,visited)



for _ in range(t):
    n,k = list(map(int,input().split()))
    visited = set()
    d_list = list(map(int,input().split())) # 건물 건설 시간 리스트
    d_stack = [[0] for _ in range(n)] # 깊이 별 모음
    graph = {i:[] for i in range(1,n+1)}

    for _ in range(k): #그래프 생성
        x,y = list(map(int,input().split()))
        graph[x].append(y)
    spot_point = int(input())

    d_stack[0] = [d_list[0]]
    check(graph[1],1,graph,d_stack,d_list,visited)
    print(d_stack)
    answer = 0
    for data in d_stack:
        answer+=max(data)
    print(answer)