
# https://www.acmicpc.net/problem/2750

n = int(input())
n_list = []
for _ in range(n):
    n_list.append(int(input()))

n_list.sort()
for n in n_list:
    print(n)