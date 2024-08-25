
# from itertools import combinations_with_replacement
# n,m = map(int,input().split())
# n_list = sorted(list(input().split()))
# comb = set(combinations_with_replacement(n_list,m))
# for c in sorted(comb):
#     print(" ".join(list(c)))

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
temp = []

def dfs(start):
    if len(temp) == m:
        print(*temp)
        return
    remember_me = 0
    for i in range(start, n):
        if remember_me != nums[i]:
            temp.append(nums[i])
            remember_me = nums[i]
            dfs(i)
            temp.pop()

dfs(0)