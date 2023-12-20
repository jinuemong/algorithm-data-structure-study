

# 올림픽

import sys

input = sys.stdin.readline

n, k = list(map(int,input().split()))

n_list = []
k_result = []
for _ in range(n):
    nation = list(map(int, input().split()))
    n_list.append([nation[0],[nation[1], nation[2] , nation[3]]])
    if nation[0] == k:
        k_result = n_list[-1][1]

n_list.sort(key = lambda data : data[1],reverse=True)

for i,n in enumerate(n_list):
    if n[1] == k_result:
        print(i+1)
        break



