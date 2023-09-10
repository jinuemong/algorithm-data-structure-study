# 멀리뛰기
# 재귀 함수로 한칸 or 두칸의 경우의 수를 구함
# 시간 초과
answer = 0
def solution(n):
    global answer
    next_field(n)
    return answer%1234567

def next_field(n):
    global answer
    if n>0:
        next_field(n-1)
        next_field(n - 2)
    elif n==0:
        answer+=1

print(solution(3))