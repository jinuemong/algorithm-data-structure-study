
# n = int(input())
# count = 0
# def find(current):
#     global count
#     if current == n:
#         count+=1
#     elif current < n:
#         find(current+1)
#         find(current+2)
#         find(current+2)
# find(0)
# print(count%10007)

n = int(input())

# dp 테이블 초기화
dp = [0] * (n + 1)

# 초기값 설정
dp[0] = 1
dp[1] = 1

# dp 테이블 갱신
for i in range(2, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 2]) % 10007

# 결과 출력
print(dp[n])