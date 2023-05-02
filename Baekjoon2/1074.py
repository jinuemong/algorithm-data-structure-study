# 문제 유형 : 재귀호출

# [ 풀이 ]
# r행 c열의 방문 순서를 출력
# -> count = 0 선언

# 2 * 2가 기본 -> 1: [0,0],2: [0,1],3: [1,0],4: [1,1]
# 위 순서로 반복

# 4 * 4인 경우 1: [0,0],[0,1],[1,0],[1,1]

# z 모양을 구성하는 4가지 방향에 대하여 차례대로 재귀적으로 호출
# 2의 1제곱 * 2의 1제곱 일 때 0,1,2,3을 재귀로 호출
# 2의 2제곱 * 2의 2제곱 일 때 0,4,8,12를 재귀로 호출
# 각 인수의 차이가 1일 때까지 재귀로 순서대로 호출하여 카운트


def findNum(n, x, y):
    global count
    # n = 2라면 탐색 값
    if n == 2:
        # 4가지 값중에 답이 있는지 확인
        if x == r and y == c:
            print(count)
            return
        count += 1

        if x == r and y + 1 == c:
            print(count)
            return
        count += 1

        if x + 1 == r and y == c:
            print(count)
            return
        count += 1

        if x + 1 == r and y + 1 == c:
            print(count)
            return
        count += 1
        return
    # 재귀 호출로 /2한 값 탐색
    findNum(n / 2, x, y)
    findNum(n / 2, x, y + n / 2)
    findNum(n / 2, x + n / 2, y)
    findNum(n / 2, x + n / 2, y + n / 2)


count = 0
N, r, c = map(int, input().split())

findNum(2**N, 0, 0) # 2의 n제곱 * 2의 n제곱 (0,0)부터 탐색

# 특정 영역을 4등분해서 반복적으로 호출
