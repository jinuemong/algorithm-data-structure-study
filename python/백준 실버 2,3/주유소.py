
# 주유소마다 다른 가격
# 1키로당 1리터의 기름 사용

n = int(input())
bridge = list(map(int,input().split()))
cost = list(map(int,input().split()))

answer = 0
min_cost = cost[0]

for i in range(n-1):
    if cost[i] < min_cost:
        min_cost = cost[i]
    answer += min_cost * bridge[i]
print(answer)