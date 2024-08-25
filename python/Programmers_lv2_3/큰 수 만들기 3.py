
# 큰 수 만들기
# k개의 수를 제거했을 때 얻을 수 있는 가장 큰 수 구하기
# 1924 -> 1,2 제거 후 94
# 작은 숫자 k개 제거, 큰 숫자 순서대로 k개 출력
# 기존의 순서는 유지되어야 함 !

# 스택 활용

def solution(number, k):
    answer = []

    for n in number:
        while k>0 and len(answer)>0 and answer[-1] < n:
            answer.pop()
            k-=1
        answer.append(n)

    return ''.join(answer[:len(answer)-k])

number = "4177252841"
k = 4
print(solution(number,k))


# 4177252841
# 775841
# 4 1 2 2 제거