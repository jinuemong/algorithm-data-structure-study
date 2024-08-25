x,y,w,s = map(int,input().split())
dp = [[0 for i in range(x+1)] for i in range(y+1)]
for i in range(x+1):
    dp[0][i] = i*w
for j in range(y+1):
    dp[j][0] = j*w
for i in range(1,y+1):
    for j in range(1,x+1):
        min_w = min(dp[i-1][j-1] + s, dp[i][j-1]+ w, dp[i-1][j]+ w)
        dp[i][j] = min_w
print(dp)
print(dp[y][x])