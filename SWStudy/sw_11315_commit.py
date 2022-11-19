T = int(input())


def goSt(n_list, di, dj, i, j):
    # di, dj는 진행 방향
    for k in range(1, 5):
        if n_list[i + di * k][j + dj * k] != 'o':
            return False
    return True


def startN(n):
    n_list = [list(input()) for _ in range(n)]
    # 다음에 있어야할 인덱스를 추가
    for i in range(n):
        for j in range(n):
            if n_list[i][j] == 'o':
                # 4개 방향 , 4개가 있는지 확인
                # 0,1 진행 방향 - 발견 시점으로 부터 오른쪽 4개 체크
                if j + 4 < n and goSt(n_list, 0, 1, i, j):
                    return True
                # 1,0 진행 방향 - 발견 시점으로 부터 아래로 4개 체크
                if i + 4 < n and goSt(n_list, 1, 0, i, j):
                    return True
                # 좌측 하단으로 진행
                if j - 4 >= 0 and i + 4 < n and goSt(n_list, 1, -1, i, j):
                    return True
                # 우측 하단으로 진행
                if j + 4 < n and i + 4 < n and goSt(n_list, 1, 1, i, j):
                    return True


for t in range(1, T + 1):
    n = int(input())
    if startN(n):
        print(f"#{t}", "YES")
    else:
        print(f"#{t}", "NO")

#출처 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXaSUPYqPYMDFASQ&categoryId=AXaSUPYqPYMDFASQ&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=3
