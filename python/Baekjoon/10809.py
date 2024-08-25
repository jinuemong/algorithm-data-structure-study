# https://www.acmicpc.net/problem/10809

arr = [-1]*26
data = input().strip()

for i in range(len(data)):
    index = ord(data[i])-ord('a')
    if arr[index]==-1:
        arr[index] = i

for a in arr:
    print(a,end=" ")