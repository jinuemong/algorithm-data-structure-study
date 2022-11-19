T = int(input())

for t in range(1,T+1):
    d,l,n = map(int,input().split())
    sum_d = 0
    for n_i in range(n):
        sum_d+=d*(1+n_i*(l/100))
    print(f"#{t}",int(sum_d))

# 출처 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXb6LR76vCcDFARR&categoryId=AXb6LR76vCcDFARR&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=3