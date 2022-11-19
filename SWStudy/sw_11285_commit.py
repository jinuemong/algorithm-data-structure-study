import math

def findR(x,y):
    r = math.ceil(math.sqrt(x*x+y*y)/20)
    if r==0:
        return 10
    elif r <=11:
        return 11-r
for t in range(1,int(input())+1):
    total = 0
    n = int(input())

    for _ in range(n):
        x,y = map(int,input().split())
        total+= findR(x,y)

    print(f"#{t}",total)


# 출처 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXZuaLsqz9wDFAST&categoryId=AXZuaLsqz9wDFAST&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=3