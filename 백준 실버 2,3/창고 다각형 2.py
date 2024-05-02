# 창고 다각형
# 좌우 탐색

import sys
input = sys.stdin.readline

m = 0
m_idx = 0
sand = [0 for _ in range(1001)]

for _ in range(int(input())):
    l,h = map(int,input().split())
    sand[l] = h
    if m < h: # max
        m_idx = l
        m = h
answer = 0
current = 0
for i in range(m_idx+1):
    current = max(current,sand[i])
    answer+=current
current = 0
for i in range(1000,m_idx,-1):
    current = max(current,sand[i])
    answer+=current
print(answer)