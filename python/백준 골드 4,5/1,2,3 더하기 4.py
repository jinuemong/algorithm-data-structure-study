

# 1a + 2b+ 3c = n을 만족하는 a,b,c의 집합

# 시간 초과
# for _ in range(int(input())):
#     n = int(input())
#     count = 0
#     for a in range(n+1):
#         for b in range(n//2+1):
#             for c in range(n//3+1):
#                 if a+2*b+3*c == n:
#                     count+=1
#                 if a+2*b+3*c > n:
#
#                     break
#     print(count)


# dp 활용

# 1로만 활용
dp = [1 for i in range(10001)]

# 2 추가
for i in range(2,10001):
    dp[i] += dp[i-2]

# 3 추가
for i in range(3,10001):
    dp[i] += dp[i-3]

for _ in range(int(input())):
    n = int(input())
    print(dp[n])