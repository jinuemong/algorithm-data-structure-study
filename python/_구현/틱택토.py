def check_win(board, player):
    # 가로, 세로, 대각선에서 승리 조건 확인
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # 가로 확인
            return True
        if all(board[j][i] == player for j in range(3)):  # 세로 확인
            return True
    if all(board[i][i] == player for i in range(3)):  # 대각선 확인
        return True
    if all(board[i][2 - i] == player for i in range(3)):  # 반대 대각선 확인
        return True
    return False


while True:
    s = input()
    if s == "end":
        break

    # 게임판 초기화
    an = [[s[i * 3 + j] for j in range(3)] for i in range(3)]
    x_count = s.count('X')
    o_count = s.count('O')

    # 기본 규칙 확인: X는 O보다 많거나 같아야 하고, 최대 1개 더 많아야 한다
    if not (x_count == o_count or x_count == o_count + 1):
        print("invalid")
        continue

    # X와 O 각각 승리 여부 확인
    x_win = check_win(an, 'X')
    o_win = check_win(an, 'O')

    # X와 O가 동시에 이길 수는 없다
    if x_win and o_win:
        print("invalid")
        continue

    # O가 이겼을 경우, X와 O의 개수가 같아야 한다
    if o_win and x_count != o_count:
        print("invalid")
        continue

    # X가 이겼을 경우, X가 O보다 1개 더 많아야 한다
    if x_win and x_count != o_count + 1:
        print("invalid")
        continue

    # 승리자가 없는 경우, 게임이 가득 찼으면 valid, 아니라면 invalid
    if not x_win and not o_win and x_count + o_count != 9:
        print("invalid")
    else:
        print("valid")