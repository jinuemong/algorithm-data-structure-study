# https://www.acmicpc.net/problem/10989

import  sys

n_list = [0]*10001

n = int(input())

for _ in range(n):
    n_list[int(sys.stdin.readline())] +=1

for i in range(len(n_list)):
    if n_list[i]>0:
        for j in range(n_list[i]):
            print(i)