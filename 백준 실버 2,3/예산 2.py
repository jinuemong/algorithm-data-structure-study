
import sys
input = sys.stdin.readline
n = int(input())
cost = list(map(int,input().split()))
sum_cost = int(input())
start,end = 0, max(cost)
while start <= end:
    mid = (start+end) //2 # 임시 예산
    total = 0
    for c in cost:
        if c > mid:
            total+=mid
        else:
            total+=c
    if total <= sum_cost:
        start = mid + 1 # 앞에서 넓이기
    else:
        end = mid -1 # 뒤에서 좁히기
print(end)

