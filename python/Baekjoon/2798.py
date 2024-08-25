# 출처 : https://www.acmicpc.net/problem/2798

n, m = map(int,input().split())
n_list = list(map(int,input().split()))
result = 0

for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            sum = n_list[i]+n_list[j]+n_list[k]
            if result<sum<=m:
                result = sum
print(result)