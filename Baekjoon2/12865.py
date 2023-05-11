
# 평범한 베낭

# n개의 물건은 W 무게, V 가치를 가짐
# 베낭에 해당 물건을 넣어서 가면 V만큼 즐김
# 최대 K만큼의 무게의 베낭

import sys
input  = sys.stdin.readline()
n ,k  = map(int,input.split())

for _ in range(n):
    w, v = map(int,input.split())
    