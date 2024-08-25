# 타고 삭제 하는 방식

import sys

import sys
input = sys.stdin.readline

def dfs(num, arr):
    arr[num] = -2
    for i in range(len(arr)):
        if num == arr[i]: #num을 부모를 가지는 것 탐색
            dfs(i, arr) #i는 자식이 됨

n = int(input())
arr = list(map(int, input().split()))
dfs(int(input()), arr)

print(len([i for i in range(len(arr)) if arr[i] != -2 and i not in arr]))
