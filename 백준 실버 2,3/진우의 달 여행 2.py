

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
        select = 0
        value = 101
        select_idx = 0
        for idx,k in enumerate(prev[j]):
            if 0<=k<j_idx:
                if value > current[k]:
                    value = current[k]
                    select = idx -1
                    select_idx = k
        search[j]=value
        prev[j] = [select_idx + i for i in [-1,0,1] if i !=select]
        print(search[j],select_idx,prev[j],end = ",")
    print()
print(search)
print(min(search))