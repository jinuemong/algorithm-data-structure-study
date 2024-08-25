# N = int(input())
# timeTable = [list(map(int, input().split())) for _ in range(N)]
#
# def solve(i):
#     if i>=N:
#         return 0
#     ret = 0
#     if i+timeTable[i][0]<=N :
#         ret = solve(i+timeTable[i][0])+timeTable[i][1]
#     ret = max(ret,solve(i+1))
#     return ret
#
# print(solve(0))
N = int(input())
TP = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

for i in range(N-1,-1,-1):
    current = i + TP[i][0]
    p = TP[i][1]
    print(i,current,p)
    if current>N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max (dp[i+1],dp[current]+p)
print(dp[0])


# i + t가 n보다 크면 탈락
# 4, 1, 10
# 4, 3, 10
# 5, 4, 20
# 7, 2, 20
# 7, 5, 15
# 10, 6, 40 x
# 9 ,7, 200 x