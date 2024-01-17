## 가장 많은 종류의 초밥을 먹어야 한다 !
## 중복이 적어야 하며, 쿠폰을 포함하지 않는 초밥을 찾는ㄷ ㅏ
import itertools
from collections import deque
import sys
input = sys.stdin.readline
n, d, k, c = map(int, input().split())
belt = deque([])
result = 0

for i in range(n): belt.append(int(input()))

for i in range(n):
    data = set(itertools.islice(belt,0,k))
    if c not in data:
        result = max(result,len(data)+1)
    else:
        result = max(result, len(data))
    belt.append(belt.popleft())
print(result)
