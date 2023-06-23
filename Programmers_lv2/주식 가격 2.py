

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
    answer,i = [len(prices)-(i+1) for i in range(len(prices))],0 #최대 값 우선 저장
    while i +1< len(answer):
        for j in range(i+1,len(answer)):
            if prices[j]<prices[i]:
                answer[i]-=(len(answer)-j-1)
                break
        i+=1
    return answer

prices =  [1, 2, 3, 2, 3]
print(solution(prices))



