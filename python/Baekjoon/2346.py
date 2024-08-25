# 출처 : https://www.acmicpc.net/problem/2346
from collections import deque

n = int(input())
n_list = list(map(int, input().split()))
n_queue = deque([[n_list[i],i+1] for i in range(0,n)])
answer = []

current , index = n_queue.popleft()
answer.append(index)

for i in range(n-1): #처음에 한번 뺌

    if current>0:
        for _ in range(current-1):
            n_queue.append(n_queue.popleft())
    else:
        for _ in range(-current):
            n_queue.appendleft(n_queue.pop())

    current,index = n_queue.popleft()
    answer.append(index)
for a in answer:
    print(a,end=" ")