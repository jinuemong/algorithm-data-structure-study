
# https://www.acmicpc.net/problem/11650

n = int(input())
n_list = []
for _ in range(n):
    n_list.append(list(map(int,input().split())))
n_list.sort()
for n in n_list: print(n[0],n[1])