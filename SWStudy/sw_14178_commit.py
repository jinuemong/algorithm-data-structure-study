T = int(input())
for t in range(1,T+1):
    answer = 0
    n, d = map(int,input().split())
    if n%(2*d+1)==0:
        answer = int(n/(2*d+1))
    else:
        answer = int(n / (2 * d + 1))+1
    print(f"#{t}",answer)



# 출처 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AX_N3oSqcyUDFARi&categoryId=AX_N3oSqcyUDFARi&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
# 리뷰 : https://jinudmjournal.tistory.com/12