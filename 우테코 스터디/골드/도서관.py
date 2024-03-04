# 도서관

n, m = map(int, input().split())

b_list = list(map(int, input().split()))
prev_list = []
next_list = []
for b in b_list:
    if b < 0:
        prev_list.append(b)
    else:
        next_list.append(b)

prev_list.sort()
next_list.sort(reverse=True)
result = 0

distance = []
for i in range(len(prev_list) // m):
    distance.append(abs(prev_list[i * m]))
if len(prev_list) % m > 0:
    distance.append(abs(prev_list[(len(prev_list) // m) * m]))

for i in range(len(next_list) // m):
    distance.append(next_list[i * m])
if len(next_list) % m > 0:
    distance.append(abs(next_list[(len(next_list) // m) * m]))

distance.sort()
result = distance.pop()
result += 2 * sum(distance)
print(result)
