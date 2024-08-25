# count = 0
#
# n = int(input())
#
# def find(current):
#     global count
#     if len(current) > n:
#         return
#     if len(current) == n:
#         count += 1
#     for i in range(int(current[-1]), 10):
#         find(current + str(i))
#
# for i in range(10):
#     find(str(i))
#
# print(count%10007)

n = int(input())

dp = [[0]*10 for _ in range(n+1)]

for j in range(10):
    dp[1][j] = 1

for i in range(2,n+1):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][k] for k in range(j+1)) % 10007

print(sum(dp[n]) % 10007)
