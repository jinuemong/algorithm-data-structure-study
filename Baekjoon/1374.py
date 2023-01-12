# https://www.acmicpc.net/problem/1374
import heapq

room = [] # 강의실
course = [] # 강의
n = int(input())

for _ in range(n):
    c = list(map(int,input().split()))
    heapq.heappush(course,[c[1],c[2]]) #시작, 끝시간

start,end = heapq.heappop(course)
heapq.heappush(room,end) # 첫 강의실 개설

for i in range(n-1):
    # 강의 순서대로 꺼내기
    start,end = heapq.heappop(course)

    # 가장 일찍 끝나는 강의 찾기
    first_end = heapq.heappop(room)

    # 강의 시간이 부족하면 개설
    if start < first_end:
        heapq.heappush(room,first_end)
        #기존 강의 재삽입
        heapq.heappush(room,end)
        # 새 강의실 개설
    # 강의 시간이 적절하면 삽입
    else:
        heapq.heappush(room,end)

print(len(room))