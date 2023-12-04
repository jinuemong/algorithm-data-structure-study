

import sys
input = sys.stdin.readline

i_idx,j_idx = list(map(int,input().split()))
step = [-1,0,1] # 0,1,2
search,prev = [] ,[[-1,j] for j in range(j_idx)]
for i in range(i_idx):
    current = list(map(int,input().split()))
    if i == 0:
        search = current
        continue
    for j in range(j_idx):
        value = 101
        next_idx = 0
        next_not_idx = 0
        for idx,k in enumerate([prev[j][1]-1,prev[j][1],prev[j][1]+1]):
            if 0<=k<j_idx and idx != prev[j][0]:
                if value > current[k]:
                    value = current[k]
                    next_idx = k
                    next_not_idx = idx
        prev[j] = [next_not_idx,next_idx]
        search[j]=value
        print(search[j],end = " ")
    print()

print(search)
print(min(search))