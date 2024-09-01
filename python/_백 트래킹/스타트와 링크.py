# 스타트팀 n/2
# 링크팀 n/2
# si += Sij + Sji ,,, 일때 si 최소의 si
# n = int(input())
# graph = []
# for _ in range(n):
#     for i in list(map(int, input().split())):
#         if i != 0:
#             graph.append(i)
# result = float("inf")
# max_depth = len(graph)
#
#
# def track(depth, left, right):
#     global result, max_depth
#     current = abs(left - right)
#     if depth == max_depth:
#         result = min(result, current)
#         return
#     track(depth + 1, left + graph[depth], right)
#     track(depth + 1, left, right + graph[depth])
# track(0,0,0)
# print(result)

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [0] * n
res = float("inf")

def DFS(l,idx):
    global res
    # 절반을 돈 경우, 남은 절반은 자동으로 다른팀
    if l == n//2:
        a = 0
        b = 0
        for i in range(n):
            for j in range(n):
                # 방문한 팀을 a로
                if visited[i] and visited[j]:
                    a += board[i][j]
                # 방문하지 않은 팀을 b로
                elif not visited[i] and not visited[j]:
                    b += board[i][j]
        # 결과 저장
        res = min(res,abs(a-b))
        return
    # 현재 인덱스부터 최대 인덱스까지 돎
    # 전에 확인한 선수 이후부터 반복
    for i in range(idx,n):
        # 방문하지 않았다면 깊이를 추가하고 idx를 추가하여 탐색한다
        if not visited[i]:
            visited[i] = True
            DFS(l+1,i+1)
            visited[i] = False
DFS(0,0)
print(res)