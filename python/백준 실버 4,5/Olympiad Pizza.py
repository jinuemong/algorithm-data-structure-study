from collections import deque

queue = deque([])

n = int(input())

for i, pizza in enumerate(list(map(int, input().split()))):
    queue.append((i, pizza))
result = [0 for i in range(n)]
count = 0
while queue:
    count += 1
    i,pizza = queue.popleft()
    if pizza ==1:
        result[i] = count
    else:
        queue.append((i,pizza-1))

for r in result:
    print(r,end=" ")
