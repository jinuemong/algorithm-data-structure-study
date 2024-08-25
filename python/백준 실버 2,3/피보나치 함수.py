

# 피보나치 함수

# f(0) = 0
# f(1) = 1
# f(2) = 1
# f(3) = 1+1 = 2
# f(4) = 1 + 2 = 3

import sys
input = sys.stdin.readline
T = int(input().rstrip())

for _ in range(T):
    data = int(input().rstrip())
    pibot_list = [0]*(data+1)
    for i in range(1,data+1):
        if i == 1: pibot_list[i] = 1
        else:
            pibot_list[i] = pibot_list[i-2]+pibot_list[i-1]
    if data == 0: print(1, 0)
    else:
        print(pibot_list[-2],pibot_list[-1])