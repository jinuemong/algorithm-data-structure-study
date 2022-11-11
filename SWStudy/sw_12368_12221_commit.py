T = int(input())
for t in range(1,T+1):
    a,b = map(int,input().split())
    if a+b ==24:
        answer = 0
    elif a+b<24:
        answer = a+b
    else:
        answer = a+b-24
    print(f"#{t}",answer)

T = int(input())
for t in range(1,T+1):
    a, b = map(int,input().split())
    if a>9 or b>9:
        answer= -1
    else:
        answer= a * b
    print(f"#{t}",answer)

# 출처 1: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXsEBlLqedsDFARX&categoryId=AXsEBlLqedsDFARX&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2
# 출처 2: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXpz3dravpQDFATi&categoryId=AXpz3dravpQDFATi&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2

# 문제풀이 :  https://jinudmjournal.tistory.com/35