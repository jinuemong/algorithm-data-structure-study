

# 재배열
# a의 수를 재배열
# b는 재배열 불가능
# 공식 : s = a인덱스 * b인덱스의 합
# 가장 작은 s를 구함
# 가장 큰 수에 가장 작은 수를 곱하게 함

import sys
input = sys.stdin.readline

n = int(input())
a_list = sorted(list(map(int,input().split())))
b_list = sorted(list(map(int,input().split())),reverse=True)
print(sum([a_list[i]*b_list[i] for i in range(n)]))