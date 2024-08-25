
# 프렌즈 4 블록 3

def solution(m, n, board):
    board = list(map(list,zip(*board)))#리스트 뒤집어서 정렬
    down_set = set([0]) # 삭제 행 모음 (실제론 열)
    answer = 0
    while down_set:
        for down in down_set:
            answer+=board[down].count("")
            new_data = list("".join(board[down]))
            board[down] = ["_" for _ in range(m-len(new_data))]+new_data
        down_set = set() # 초기화
        for j in range(n-1): # n이 이제 행
            for i in range(m-1): # m이 이제 열
                if board[i][j] != "_" and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    board[i][j], board[i+1][j], board[i][j+1] ,board[i+1][j+1] = "","","",""
                    down_set.add(j)
                    down_set.add(j+1)
    print(board)
    return answer



m,n = 6,6
board  = 	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

print(solution(m,n,board))