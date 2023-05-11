
# LCS : Longest Common Subsequence

# 최장 공통 부분 수열
# 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것

x = list(input())
x_len = len(x)
y = list(input())
y_len = len(y)

result = [[0]*(y_len+1) for _ in range(x_len+1)]

for i in range(1,x_len+1):
    for j in range(1,y_len+1):
        if x[i-1] == y[j-1]:
            result[i][j] = result[i-1][j-1]+1
        else:
            result[i][j] = max(result[i][j-1],result[i-1][j])

print(result[len(x)][len(y)])



