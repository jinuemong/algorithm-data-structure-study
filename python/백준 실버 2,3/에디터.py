from collections import deque
prev = list(input())
next = deque([])
for _ in range(int(input())):
    commend = list(input().split())
    code = commend[0]
    if code == 'L':
        if len(prev) > 0:
            next.appendleft(prev.pop())
    elif code == 'D':
        if len(next) > 0:
            prev.append(next.popleft())
    elif code == 'B':
        if len(prev) > 0:
            prev.pop()
    else:
        prev.append(commend[1])
print(''.join(prev+list(next)))