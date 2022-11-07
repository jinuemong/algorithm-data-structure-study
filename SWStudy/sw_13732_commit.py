T = int(input())


def explore(n,n_list):
    check_list = [[] for i in range(n)] #최대 n 길이의 정사각형

    for i in range(n):
        for j in range(n):
            if n_list[i][j]=="#":
                check_list[i].append([i,j])

    check_len_i, check_len_j = 0,0

    for i in range(len(check_list)):
        if len(check_list[i])>0: #변 발견
            check_len_j+=1
            if check_len_i==0: #길이가 없다면 길이 산정
                check_len_i = len(check_list[i])

                if len(check_list)==1 and check_len_i==1:
                    return True #길이가 모두 1이면 # 하나
            else:
                if check_len_i!=len(check_list[i]):
                    return False #길이가 다르면 False 반환
                else:
                    check_index = check_list[i][0][0]
                    for k in range(len(check_list[i])-1):
                        if check_list[i][k][0]!=check_index:
                            return False # 앞자리가 다르면 False
                        if (check_list[i][k][1]+1)!= check_list[i][k+1][1]:
                            return False # 연속성 없으면 False

    if check_len_i!=check_len_j: #좌우 다름
        return False
    else:
        return True

for t in range(1, T + 1):
    n = int(input())
    n_list = [list(input()) for i in range(0, n)]

    if explore(n,n_list):
        print(f"#{t}", "yes")
    else:
        print(f"#{t}", "no")


# 출처 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AX8BAN1qTwoDFARO&categoryId=AX8BAN1qTwoDFARO&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

# 개인 문제풀이 : https://jinudmjournal.tistory.com/23