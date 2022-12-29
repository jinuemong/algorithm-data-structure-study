# https://www.acmicpc.net/problem/11286

# 0이 주어진 경우 출력 값 담음 -> 배열에 아무것도 없으면 0 출력
# 0이 아니라면 배열을 채움
# 출력 시 절대값이 제일 작은 값 출력 후 제거
# 절대값이 같으면 -수 출력 후 제거
import sys
import heapq
input = sys.stdin.readline



n = int(input())
heap = []
answer = []
for _ in range(n):
    x= int(input())
    if x ==0:
        if len(heap)== 0:
            print(0)
        else:
            absolute, normal = heapq.heappop(heap)
            print(normal)
    else:
        heapq.heappush(heap,(abs(x),x))