T = int(input())


def explore(n,n_list):
    check_list = []
    for i in range(n):
        for j in range(n):
            if n_list[i][j]=="#":
                check_list.append([i,j])

    i = 0
    check_len = 0 # #이 발견된 지점부터 가로 길이

    while i<len(check_list):
        if check_len==0:
            check_len=1
            current_i = check_list[i][0]
            current_j = check_list[i][1]
            while True:
                i += 1
                if i == len(check_list):   # 끝 지점일 시 종료
                    break
                if current_i == check_list[i][0]:
                    check_len += 1
                else:
                    break
            print(current_i,current_j,check_len)
            # 길이가 1인 경우 상하좌우로 아무것도 있으면 안됨
            if check_len==1:
                if n_list[current_i][current_j+1]=='#' or n_list[current_i+1][current_j+2]=='#'\
                        or n_list[current_i+1][current_j]=='#' or n_list[current_i+2][current_j+1]=='#':
                    return False
            # 그 외는 check_len * check_len 만큼 #가 있어야함
            else:
                for c_i in range(current_i, current_i + check_len):
                    for c_j in range(current_j, current_j + check_len):
                        print(c_i,c_j)
                        if n_list[c_i][c_j]!="#":
                            return False

            check_len = 0
            i+=1
    return True


for t in range(1, T + 1):
    n = int(input())
    n_list = [list(input()) for i in range(0, n)]

    if explore(n,n_list):
        print(f"#{t}", "yes")
    else:
        print(f"#{t}", "no")


