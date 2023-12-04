
import sys
input = sys.stdin.readline
n = int(input())
cost = sorted(list(map(int,input().split())),reverse=True)
sum_cost = int(input())
max_location_idx = cost[0]
if sum(cost) < max_location_idx:
    print(cost[0])
else:
    for idx, c in enumerate(cost):
        if c * n < sum_cost:
            max_location_idx = idx
            break

    sum_cost -= sum(cost[max_location_idx:])
    data = cost[max_location_idx]

    while data < cost[0]:
        if sum_cost < (data+1)*max_location_idx:
            break
        data+=1
    print(data)

