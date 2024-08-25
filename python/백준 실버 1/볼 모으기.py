#
# from collections import deque
#
# n  = int(input())
#
# balls = list(input())
#
# count_r = 0
# queue = deque(balls)
# while queue:
#     if queue[-1] == "R":
#         queue.pop()
#     else:
#         if queue[0] == "R":
#             count_r+=1
#         queue.popleft()
# count_b = 0
# queue = deque(balls)
# while queue:
#     if queue[-1] == "B":
#         queue.pop()
#     else:
#         if queue[0] == "B":
#             count_b+=1
#         queue.popleft()
# print(min(count_r,count_b))

# n = int(input())
# balls = list(input())
#
# ball_r, ball_b = 0, 0
# r_flag, b_flag = False, False
# for i in range(len(balls) - 1, -1, -1):
#     if balls[i] == "R":
#         if r_flag:
#             ball_r += 1
#     else:
#         r_flag = True
#
#     if balls[i] == "B":
#         if b_flag:
#             ball_b += 1
#     else:
#         b_flag = True
#
# print(min(ball_r, ball_b))

# n = int(input())
# balls = input()
#
# red = balls.count("R")
# blue = n - red
#
# res = min(red,blue)
#
# cont = 1
#
# for i in range(1,n):
#     if balls[i] == balls[i-1]:
#         cont+=1
#     else:
#         break
#
# if balls[0] == 'R':
#     res = min(res, red - cont)
# else:
#     res = min(res, blue - cont)
#
# cont = 1
#
# for i in range(n-2,-1,-1):
#     if balls[i] == balls[i+1]:
#         cont+=1
#     else:
#         break
#
# if balls[-1] == 'R':
#     res = min(res, red - cont)
# else:
#     res = min(res, blue - cont)

import sys

input = lambda: sys.stdin.readline().rstrip()
def move_balls(type_of_ball_to_move,s):
    s=s.lstrip(type_of_ball_to_move)
    return s.count(type_of_ball_to_move)

n = int(input())
s=input()
print(min(
    move_balls("R",s),
    move_balls("R",s[::-1]),
    move_balls("B",s),
    move_balls("B",s[::-1])))
