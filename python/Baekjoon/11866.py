# https://www.acmicpc.net/problem/11866
from collections import deque
n , k = list(map(int,input().split()))
arr = deque([i for i in range(1,n+1)])
print("<",end="")
while len(arr)>0:
    for i in range(k-1):
        arr.append(arr.popleft())
    if len(arr)==1:
        print(arr.popleft(), end=">")
    else:
        print(arr.popleft(),end=", ")
