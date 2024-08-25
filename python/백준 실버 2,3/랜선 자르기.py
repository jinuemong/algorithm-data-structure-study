import sys
input = sys.stdin.readline
k, n = map(int, input().split())
k_list = [int(input()) for _ in range(k)]
start, end = 1, max(k_list) # end = 가장 큰 수

while start <= end:
    mid = (start + end) // 2
    count = 0
    for v in k_list:
        count += v//mid
    if count >= n :
        start = mid + 1
    else:
        end = mid -1
print(end)