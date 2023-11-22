import sys
input = sys.stdin.readline
r1, c1, r2, c2 = list(map(int, input().split()))
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
hurricane = [[0 for _ in range(c2 - c1 + 1)] for _ in range(r2 - r1 + 1)]
total = (c2 - c1 + 1) * (r2 - r1 + 1)
x, y = 0, 0
cnt, repeat_count, d = 1, 1, 0
num = 1

while total > 0:

    if r1 <= y <= r2 and c1 <= x <= c2:
        total -= 1
        hurricane[y - r1][x - c1] = num  # 원점에서 (r1,c1) 떨어진 거리로 이동
    num += 1
    if repeat_count == 0:
        cnt += 1
        d += 1
        if cnt % 2 == 0:
            repeat_count = int(cnt / 2)
        else:
            repeat_count = int((cnt + 1) / 2)
    repeat_count -= 1
    y = y + dy[d % 4]
    x = x + dx[d % 4]

max_num_len = len(str(num-1))
for i in range(len(hurricane)):
    for j in range(len(hurricane[0])):
        print(str(hurricane[i][j]).rjust(max_num_len),end =' ')
    print()