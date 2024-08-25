

# 2 * n 타일링
# 2 * 1 의 타일이 있음
# 1* 2 or 2 * 1 변환 가능
# 2 * n인 바닥을 가득 채우는 수
# 총 경우의 수 출력
# 높이가 2이므로
# 길이가 1이거나 2인 경우를 선택해서 n을 만드는 경우의 수
# Ex n = 4
# 1 1 1 1 , 1 1 2 , 1 2 1 , 2 1 1, 2 2
# n이 최대 60000
answer = 0
def solution(n):
    global answer
    answer = 0
    dfs(n)
    return answer % 1000000007
def dfs(n):
    global answer
    if n > 0:
        dfs(n-1)
        dfs(n-2)
    if n==0:
        answer+=1

for n in range(1,10):
    print(solution(n))

