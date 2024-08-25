import sys; input = sys.stdin.readline

def ccw(a, b, c):
    return (a[0] * b[1] + b[0] * c[1] + c[0] * a[1]) - (a[1] * b[0] + b[1] * c[0] + c[1] * a[0])

def solve():
    N = int(input())
    if N < 3: # 빌딩이 1개나 2개면 보이는 빌딩은 0개나 1개다.
        print(N - 1)
        return
    H = list(map(int, input().split()))

    answer = 0
    # 모든 빌딩마다 보이는 빌딩의 수를 구해야 한다.
    for i in range(N):
        result = []
        # 왼쪽
        if 0 < i: # 기준 빌딩의 index가 0보다 커야 한다.
            result.append(i - 1)
            for j in range(i - 2, -1, -1):
                if ccw([i, H[i]], [result[-1], H[result[-1]]], [j, H[j]]) < 0:
                    result.append(j)
        # 오른쪽
        if i < N - 1: # 기준 빌딩의 index가 N - 1보다 작아야 한다.
            result.append(i + 1)
            for j in range(i + 2, N):
                if ccw([i, H[i]], [result[-1], H[result[-1]]], [j, H[j]]) > 0:
                    result.append(j)
        answer = max(answer, len(result))
    print(answer)

solve()