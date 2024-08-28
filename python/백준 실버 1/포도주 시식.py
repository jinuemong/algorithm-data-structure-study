
# 연속 3잔을 마실 수 없다
# 최대 양
# 3가지 경우 고려
# 이전 것 선택 -> 1전 합
# 지금 선택 -> 2전 합
# 이전 것과 지금 선택 -> 3전 합
n = int(input())
podo = [0]
for _ in range(n):
    podo.append(int(input()))
dp = [0] * (n+1)
dp[1] = podo[1]
if n > 1:
    dp[2] = podo[1] + podo[2]

for i in range(3,n+1):
    dp[i] = max(dp[i-2]+podo[i],dp[i-1],dp[i-3]+podo[i-1]+podo[i])
print(dp[n])
