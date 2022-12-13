#https://www.acmicpc.net/problem/10773

import sys

k = int(sys.stdin.readline().strip())
stack,sum = [], 0
for _ in range(k):
    n = int(sys.stdin.readline().strip())
    if n==0:
        sum-=stack.pop()
    else:
        stack.append(n)
        sum+=n
print(sum)