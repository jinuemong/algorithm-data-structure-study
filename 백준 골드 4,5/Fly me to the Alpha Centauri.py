import sys

input = sys.stdin.readline
def drf(depth,current,prev,end):
    print(depth,current,prev,end)
    if end == current:
        print(depth)
    elif end>current:
        for next in range(prev-1,prev+2):
           if current < next+current:
                drf(depth+1,current+next,next,end)

for _ in range(int(input())):
    start,end = list(map(int,input().split()))
    drf(0,start,0,end)
