T = int(input())

for t in range(1,T+1):
    a, b = 1, 1
    s = list(input())
    for s_i in s:
        if s_i=="L":
            b = a+b
        else:
            a = a+b
    print(f"#{t}",a,b)

# 출처 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXgZSOn6ApIDFASW&categoryId=AXgZSOn6ApIDFASW&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=3