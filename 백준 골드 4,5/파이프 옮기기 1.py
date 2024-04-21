# (0,1) -> 0,1 1,1
# (1,0) -> 1,0 1,1
# (1,1) -> 0,1 1,0 1,1
# 1이면 이동 안함
# 0,1 부터 시작
# direction = {(0, 1), (1, 0)}
# ans = 0
# n = int(input())
# n_list = [list(map(int, input().split())) for _ in range(n)]
# stack = [((0, 1), (0, 1))]
# while stack:
#     current, next = stack.pop()
#     for y, x in direction - {next} | {(1, 1)}:
#         dy, dx = current[0] + y, current[1] + x
#         if 0 <= dy < n and 0 <= dx < n  and n_list[dy][dx] == 0:
#             stack.append(((dy, dx), (y, x)))
#         elif dy == n - 1 and dx == n - 1:
#             ans += 1
# print(ans)

n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]

# dp[y][x][state]: (y, x) 위치에 state 상태로 파이프가 놓여 있는 경우의 수
# state: 0 - 가로, 1 - 세로, 2 - 대각선
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]

# 초기 파이프 상태: 가로로 (1, 1)과 (1, 2) 차지
if house[0][0] == 0 and house[0][1] == 0:
    dp[0][1][0] = 1

# DP를 사용하여 각 위치에서 각 상태의 가능한 이동 계산
for y in range(n):
    for x in range(n):
        if house[y][x] == 0:
            # 가로 -> 가로, 대각선
            if x + 1 < n and house[y][x + 1] == 0:
                dp[y][x + 1][0] += dp[y][x][0] + dp[y][x][2]
            # 세로 -> 세로, 대각선
            if y + 1 < n and house[y + 1][x] == 0:
                dp[y + 1][x][1] += dp[y][x][1] + dp[y][x][2]
            # 대각선 -> 가로, 세로, 대각선
            if x + 1 < n and y + 1 < n and house[y + 1][x + 1] == 0 and house[y + 1][x] == 0 and house[y][x + 1] == 0:
                dp[y + 1][x + 1][2] += dp[y][x][0] + dp[y][x][1] + dp[y][x][2]

# 결과는 (n, n) 위치에 파이프 한쪽 끝이 도달하는 경우의 수
print(sum(dp[n-1][n-1]))