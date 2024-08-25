T = int(input())
for n in range(1,T+1):
    is_possible = True
    b_index= "x"
    n_index = "x"
    n,m = map(int , input().split()) #격자판 크기
    nm = [' ']*n # 빈 격자판
    for k in range(0,n):
        nm[k] = list(input())[0:m]
        if b_index=="x":
            if nm[k].index("#"):
                if nm[k].index("#")%2==0:
                    b_index = "짝"
                else:
                    b_index="홀"
                if k%2==0:
                    n_index = "짝"
                else:
                    n_index = "홀"
            if nm[k].index("."):
                if nm[k].index(".")%2==0:
                    b_index = "홀"
                else:
                    b_index = "짝"
                if k%2==0:
                    n_index = "짝"
                else:
                    n_index = "홀"

    if is_possible:
        print("#"+str(n),"possible")
    else:
        print("#"+str(n),"impossible")




