

# 제곱수 찾기
# 행 & 열 등차 조건
# 같은 행이 증&감 하거나 열이 증&감 한다 (행 or 열 = 0으로 등차 성립)
# -> 직선 등차
# 행과 열이 모두 증&감
# -> 대각선 등차

# 탐색 알고리즘 사용 !?

# 제곱수 조건 !
# 맨 뒤 자리가 홀수가 올 수 없음
import sys
from itertools import permutations
input = sys.stdin.readline
n,m = list(map(int,input().split()))
res = -1
n_list = [list(input().strip()) for _ in range(n) ]

def find(i,j):
    data_set = [
        [n_list[i][y] for y in range(j, len(n_list[0]))], # left
        [n_list[x][j] for x in range(i, len(n_list))], # right
        [n_list[i + x][j + x] for x in range(min(len(n_list) - i, len(n_list[0]) - j))] #mid
    ]
    for data in data_set:
        for idx in range(1,len(data)):
            value = int("".join([x for x in range(0,len(data),idx)]))
            if (value**0.5)**2 == value:
                res = max(value,res)


for i in range(len(n_list)):
    for j in range(len(n_list[0])):
        find(i,j)

