
# 주식 가격

# 안떨어진 횟수 : 시작된 직후와 전은 안떨어짐
# s  1 2 3 2 3 [i]
# 1  4 (n-1)
# 2  4 3 (n-2)
# 3  4 2 2 (n-3)
# 2  4 2 1 1 (n-4)
# 3  4 2 1 1 0 (n-5)
#[j]
def solution(prices):
    answer = [len(prices)-1 for _ in range(len(prices))]
    for i in range(len(prices)):
        for j in range(1,len(prices)):
            if i ==j:
                answer[i] = len(prices)-j-1
            elif prices[i]> prices[j]:
                answer[i] -=1
    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))




