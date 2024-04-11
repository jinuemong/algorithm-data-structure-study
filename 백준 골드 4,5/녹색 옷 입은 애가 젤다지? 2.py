# 시간초과로 다시풀기
# heapq 활용
import heapq
import sys
input = sys.stdin.readline

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n = int(input())
count = 0

while n != 0:
    count+=1
    n_list = [list(map(int,input().split()))for _ in range(n)]
    visited = [[float("inf")]*n for i in range(n)]
    heap = []
    visited[0][0] = n_list[0][0]
    heapq.heappush(heap, (n_list[0][0],0,0))
    while heap:
        distance, i,j = heapq.heappop(heap)
        if i == n-1 and j == n-1:
            print("Problem " + str(count) + ": " + str(distance))
            n = int(input())
            break
        for dx, dy in direction:
            x, y = i + dx, j + dy
            if 0 <= x < n and 0 <= y < n and visited[x][y] > distance + n_list[x][y]:
                visited[x][y] = distance + n_list[x][y]
                heapq.heappush(heap,(distance + n_list[x][y],x,y))