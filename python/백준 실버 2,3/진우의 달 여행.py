

import sys
input = sys.stdin.readline

i_idx,j_idx = list(map(int,input().split()))

search,prev = [] ,[[j-1,j,j+1] for j in range(j_idx)]

for i in range(i_idx):

    current = list(map(int,input().split()))
    if i == 0:
        search = current
        continue
    for j in range(j_idx):
        print(prev)
        prev_idx,current_idx, current_value = 0,0,101
        for idx,s in enumerate(prev[j]):
            if 0<=s<j_idx:
                if current_value > current[s]:
                    prev_value = current[s]
                    current_idx = s
                    prev_idx = idx
        prev[j] = [current_idx+i for idx,i in enumerate([-1,0,1]) if idx != prev_idx ]
        search[j]+= current_value

print(min(search))