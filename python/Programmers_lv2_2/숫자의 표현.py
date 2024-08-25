


# 숫자의 표현
# 자연수를 합의 조합으로 나타내기
# 연속 된 수이므로 1씩 차이남
# n = 1 : 1 = 1 ( 1)
# n = 2 : 1 = 1 ( 1)
# n = 3 : 1 + 2 = 3, 3 = 3 ( 2)
# n = 4 : 4 = 4 ( 1)
# n = 5 : 2 + 3 = 5, 5 = 5 ( 2)
# n = 6 : 1 + 2 + 3 = 6, 6 = 6 ( 2)
# n = 7 : 3 + 4 = 7 , 7 = 7 ( 2)
# n = 8 : 8 = 8 ( 1)
# n = 9 : 2 + 3 + 4, 4 + 5, 9 ( 3)


def solution(n):
    answer  = 0
    for i in range(1,n+1):
        sum = 0
        for j in range(i,n+1):
            sum+=j
            if sum == n:
                answer+=1
                break
            elif sum > n:
                break
    return answer

n = 15
print(solution(n))