T = int(input())

for n in range(1,T+1):
    is_possible = True # 가능성 확인
    n,m = map(int, input().split()) #체스판 크기
    nm = [' '] * n  # 빈 격자판
    check_nm = {".짝":0,".홀":0,"#짝":0,"#홀":0} #격자판 위치 체크
    for k in range(0,n):
        nm[k] = list(input())

    for n_ in range(n):
        for m_ in range(m):
            index_sum = n_+m_
            if nm[n_][m_] == '.': #흰색
                if (index_sum) % 2 == 0:
                    check_nm[".짝"]+=1
                elif (index_sum) % 2 == 1:
                    check_nm[".홀"]+=1
            elif nm[n_][m_]=='#': #검은색
                if (index_sum) % 2 == 0:
                    check_nm["#짝"]+=1
                elif (index_sum) % 2 == 1:
                    check_nm["#홀"]+=1

    if (check_nm["#짝"]>0 and check_nm["#홀"]>0) \
            or (check_nm[".짝"]>0 and check_nm[".홀"]>0) \
        or (check_nm[".짝"]>0 and check_nm["#짝"]>0) \
        or (check_nm[".홀"]>0 and check_nm["#홀"]>0):
        is_possible = False
    if is_possible:
        print("#"+str(n),"possible")
    else:
        print("#"+str(n),"impossible")

# 출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYEXgKnKKg0DFARx
# 리뷰: https://jinudmjournal.tistory.com/11