
import sys
input = sys.stdin.readline

n = int(input())
n_list = [list(map(int,input().split()))for i in range(n)]
n_list.sort(key = lambda x: (x[1],x[0]))
count = 0
prev = 0
for start,end  in n_list:
    if prev <=start:
        count+=1
        prev = end

print(count)