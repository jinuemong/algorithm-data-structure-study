
# https://www.acmicpc.net/problem/1427

n = list(map(int,input()))
n.sort(reverse=True)

for i in n: print(i,end='')