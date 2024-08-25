# 출처 : https://www.acmicpc.net/problem/5397
# 문제 풀이
t = int(input())

for _ in range(t):
    com = list(input())
    left_stack, right_stack = [], []
    for c in com:
        if c == '-':
            if left_stack:
                left_stack.pop()
        elif c == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif c == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(c)
    answer = "".join(left_stack)
    # right_stack 은 거꾸로 쌓임
    print(answer+"".join(reversed(right_stack)))
