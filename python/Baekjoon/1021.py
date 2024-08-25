# https://www.acmicpc.net/problem/1021
# 풀이

from collections import deque
n, m = list(map(int,input().split()))

n_list = list(map(int,input().split()))
arr = deque([i for i in range(1,n+1)])
count = 0
def goLeft():
    arr.append(arr.popleft())
def goRight():
    arr.appendleft(arr.pop())

for a in n_list:
    index = arr.index(a)
    if index<=len(arr)//2:
        for i in range(index):
            goLeft()
            count+=1
    else:
        for i in range(len(arr)-index):
            goRight()
            count+=1
    arr.popleft()

print(count)
