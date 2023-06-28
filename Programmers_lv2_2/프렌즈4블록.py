
# 프렌즈 4 블록

def solution(m, n, board):
    board = [list(board[b]) for b in range(m)]
    down_dic = {0:[0,0]} # 삭제 인덱스 모음 x,y 는 삭제 인덱스 위치
    answer = -1
    # min(x) ~ max(y) : 값이 있을 시
    # x ~ y : 값이 없을 시
    # 두 값을 삭제 한 만큼 위에서 끌어오기
    # -> 빈 위치 -> 빈 위치 크기 만큼 위에서 끌어오기 -> 위칸 공백으로 전환
    while down_dic:
        for key,value in down_dic.items(): #삭제 된 위치 변환
            y_len = (value[1] - value[0])+1 # 총 삭제 인덱스 길
            for i in range(0,value[0]):
                if value[0]<=i+y_len<=value[1]:
                    board[i+y_len][key] = board[i][key]
                board[i][key] == " "
            answer += y_len  # 빈 자리를 매우는 과정이므로 + 1
        down_dic.clear()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != " " and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    if j in down_dic: # 키 존재
                        down_dic[j][0] = min(down_dic[j][0], i)
                        down_dic[j][1] = max(down_dic[j][1],i+1)
                    else:
                        down_dic[j] = [i,i+1]
                    if j+1 in down_dic: # 키 존재
                        down_dic[j+1][0] = min(down_dic[j+1][0], i)
                        down_dic[j+1][1] = max(down_dic[j+1][1],i+1)
                    else:
                        down_dic[j+1] = [i,i+1]
    return answer

m,n = 4,5
board  = 	["CCBDE", "AAADE", "AAABF", "CCBBF"]

print(solution(m,n,board))