
# https://www.acmicpc.net/problem/10814

# 나이, 가입 순서, 이름 순으로 저장

n = int(input())
n_list = []
for i in range(n):
    age,name= input().split()
    n_list.append([int(age),i,name])

n_list.sort()
for n in n_list: print(n[0],n[2])