def solution(n, m, section):
    answer = 0

    section = set(section)
    i = 1
    while i < n+1:
        if i in section:
            i+=m
            answer +=1
        else:
            i+=1

    return answer

# 1~ n 까지의 번호
# 페인트를 다시 칠해야 하는 벽
# 롤러의 길이 : m 미터
# [2가지 규칙]
# 롤러가 벽을 벗어나면 안됨, 구역의 일부분만 포함되도록 칠하면 안됨
# 최소한의 페인트로 주어진 section을 모두 칠해야 함
n = 8
m = 4
section = [2,3,6]
print(solution(n,m,section))