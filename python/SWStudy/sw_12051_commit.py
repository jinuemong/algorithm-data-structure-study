T = int(input())

for t in range(1,T+1):
    n,Pd,Pg = map(int,input().split())

    #만약 최종이 0프로일 때 오늘이 0프로가 아니거나
    #최종이 100프로일 때 오늘이 100프로가 아니면 절대 불가능
    # 테스트 케이스 줄이기
    if (Pg==0 and Pd!=0) or (Pg==100 and Pd!=100):
        print(f"#{t}","Broken")
    else:
        isPossible = False

        for d in range(1,n+1):
            if (d*Pd/100).is_integer():
                isPossible= True
                break

        if isPossible:
            print(f"#{t}", "Possible")
        else:
            print(f"#{t}", "Broken")

# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXmwMidaSLIDFARX&categoryId=AXmwMidaSLIDFARX&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2
