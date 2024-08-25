T = int(input())

for t in range(1, T + 1):
    n = int(input())
    n_list = list(map(int, input().split()))
    count = 0
    for i in range(1, n - 1):
        if n_list[i] != max(n_list[i - 1], n_list[i], n_list[i + 1]) \
                and n_list[i] != min(n_list[i - 1], n_list[i], n_list[i + 1]):
            count += 1
    print(f"#{t}", count)

# 출처 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXhh-H-KwUcDFARQ&categoryId=AXhh-H-KwUcDFARQ&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2