
# 로봇 청소기

# (0,0)
# (n-1, m-1)

# 반시계 방향으로 회전

# 방향 순서 0 -> 3 -> 2 -> 1
# (-1,0) > (0,-1) > (1,0) > (0,1)
d_list = [(-1,0),(0,-1),(1,0),(0,1)] # current%4
n,m = map(int,input().split())
i,j,d = map(int,input().split())
nm = []
count = 0
for k in range(n):
    nm.append(list(map(int,input().split())))

while 0<=i<n and 0<=j<m:
    if nm[i][j] == 0:
        nm[i][j] = 1
        count +=1
        continue
    check = False
    for k in d_list:
        if (0<=i+k[0]<n and 0<=j<m) and nm[k[0]+i][k[1]+j] == 0:
            check = True
    if check:
        d+=1
        next_i = d_list[d%4][0] + i
        next_j = d_list[d%4][1] + j
        if 0<=next_i<n and 0<=next_j<m:
            if nm[next_i][next_j] == 0:
                i = next_i
                j = next_j
                nm[i][j] = 1
                count += 1
    else:
        tmp = d_list[(d+2)%4]
        if 0<=i+tmp[0]<n and 0<=j+tmp[1]<m:
            i+=tmp[0]
            j+=tmp[1]
        else:
            break
print(count)