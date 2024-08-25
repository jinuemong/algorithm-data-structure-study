# https://www.acmicpc.net/problem/2953

index,max = 0,0

for i in range(1,6):
    s = sum(list(map(int,input().split())))
    if max<s:
        index = i
        max = s
print(index,max)