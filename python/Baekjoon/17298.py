# 출처 : https://www.acmicpc.net/problem/17298
# 포스팅
# 시간초과
import sys

n = int(sys.stdin.readline().strip())

n_list = list(map(int,sys.stdin.readline().strip().split()))
for i in range(0,n-1):
    k = -1
    for j in range(i,n):
        if n_list[i]<n_list[j]:
            k = n_list[j]
            break
    print(k, end=' ')
print(-1)
