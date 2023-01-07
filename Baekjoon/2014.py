# https://www.acmicpc.net/problem/2014
# 리뷰
import heapq
k, n = list(map(int,input().split()))
n_list = list(map(int,input().split()))

heap = [] # 우선 순위 큐를 위함
vist = set() # 이미 처리 됨
max_value = max(n_list) #가장 큰 수를 구해둠
# 제일 처음 수를 꺼내서 각 원소의 곱을 넣어줌

for x in n_list: #초기 값 넣어줌
    heapq.heappush(heap,x) 

# n-1 번째 까지 뽑고 마지막에 n번째를 출력
for i in range(n-1):
    element = heapq.heappop(heap)

    for x in n_list:
        now = element*x # 곱결과 계산

        if len(heap)>=n and max_value < now:
            continue
        # 크기가 n이상이면 초과
        # 가장 큰 수 보다 현재n_list 뽑은 수가 크다면 신경x

        if now not in vist:
            heapq.heappush(heap,now)
            max_value = max(max_value,now)
            vist.add(now)

print(heapq.heappop(heap))

