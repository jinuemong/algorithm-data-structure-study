import sys
input = sys.stdin.readline

for _ in range(int(input())):
    start,end = list(map(int,input().split()))
    count = 0
    next = 1
    while start<end:
        count += 1
        if start+1 == end:
            break
        for i in range(next,0,-1):
            if start+i<=end:
                start+=i
                break
        next = count
    print(count)
