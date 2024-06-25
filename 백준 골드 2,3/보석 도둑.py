
import heapq
n,k = map(int,input().split())
stone = []
for i in range(n):
    m,v  = map(int,input().split())
    stone.append([-v,m])
bag = sorted([int(input()) for _ in range(k)])

heapq.heapify(stone)
price = 0
for size in bag:
    if len(stone) ==0:
        break
    while len(stone) > 0:
        v,m = heapq.heappop(stone)
        if m <= size:
            price += -v
            break
print(price)

