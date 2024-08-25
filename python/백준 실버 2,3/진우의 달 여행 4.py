

import sys
input = sys.stdin.readline

i_idx,j_idx = list(map(int,input().split()))
step = [-1,0,1] # 0,1,2
search,prev = [] ,[[-1,j] for j in range(j_idx)]
space = [list(map(int,input().split())) for i in range(i_idx)]
min_value = sys.maxsize

def drf(prev_step,prev_idx,i,value):
    global min_value,space
    if i == i_idx:
        min_value = min(value,min_value)
        return
    for idx,k in enumerate([prev_idx-1,prev_idx,prev_idx+1]):
        if 0<=k<j_idx and idx != prev_step:
            drf(idx,k,i+1,value+space[i][k])

for j in range(j_idx):
    drf(-1,j,1,space[0][j])

print(min_value)