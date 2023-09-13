

# 124 나라의 숫자

def solution(n):
    answer = ""
    while n:
        print(n)
        if n % 3:
            answer = str(n%3) + answer
            n//=3
        else:
            answer = "4" + answer
            n = n//3-1
    return answer

print(solution(10))