T = int(input())

for t in range(1,T+1):
    s = list(input())
    s_set = set(s)
    isYes = True

    for s_i in s_set:
        if s.count(s_i)!=2:
            isYes = False
            break

    if isYes:
        print(f"#{t}", "Yes")
    else:
        print(f"#{t}", "No")


# 출처 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXjS1GXqZ8gDFATi&categoryId=AXjS1GXqZ8gDFATi&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2
