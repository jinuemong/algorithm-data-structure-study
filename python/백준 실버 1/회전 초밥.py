## 가장 많은 종류의 초밥을 먹어야 한다 !
## 중복이 적어야 하며, 쿠폰을 포함하지 않는 초밥을 찾는ㄷ ㅏ

n, d, k, c = map(int, input().split())

from collections import deque

belt = deque([])
prev = deque([])
result = 0
for i in range(n):
    belt.append(int(input()))
    if k < len(belt):
        prev.append(belt.popleft())
    if len(belt) == k:
        belt_set = set(belt)
        if len(belt_set) == k:
            if c not in belt_set and len(belt_set) <= d:
                result = max(result, k + 1)
            else:
                result = max(result, k)

for data in prev:
    belt.popleft()
    belt.append(data)
    if len(belt) == k:
        belt_set = set(belt)
        if len(belt_set) == k:
            if c not in belt_set and len(belt_set) <= d:
                result = max(result, k + 1)
            else:
                result = max(result, k)
print(result)
