def findP(places_list, x, y, dx, dy):
    if places_list[y + dy][x + dx] == 'P':
        if dx + dy == 1:  # 단순 우,하 확인 (0,1) or (1,0)
            return True

        elif dx == 2:  # 우 사이가 O인지 확인
            if places_list[y][x + 1] == 'O':
                return True
        elif dy == 2:  # 하 사이가 O인지 확인
            if places_list[y + 1][x] == 'O':
                return True
        else:
            if dx == -1:
                if places_list[y][x - 1] == 'O' or places_list[y + 1][x] == 'O':
                    return True
            else:
                if places_list[y][x + 1] == 'O' or places_list[y + 1][x] == 'O':
                    return True

    return False


def solution(places):
    answer = []
    for answer_i in range(5):
        current_answer = 1

        for y in range(5):
            if current_answer == 0:
                break
            for x in range(5):
                if places[answer_i][y][x] == "P":
                    # 우측 확인
                    if x + 1 < 5 and findP(places[answer_i], x, y, 1, 0):
                        current_answer = 0
                        break
                    # 하단 확인
                    if y + 1 < 5 and findP(places[answer_i], x, y, 0, 1):
                        current_answer = 0
                        break
                    # 좌측 하단 확인
                    if x - 1 >= 0 and y + 1 < 5 and findP(places[answer_i], x, y, -1, 1):
                        current_answer = 0
                        break
                    # 우측 하단 확인
                    if x + 1 < 5 and y + 1 < 5 and findP(places[answer_i], x, y, 1, 1):
                        current_asnwer = 0
                        break
                    # 한 칸 건너 우측 확인
                    if x + 2 < 5 and findP(places[answer_i], x, y, 2, 0):
                        current_answer = 0
                        break
                    # 한 칸 건너 하단 확인
                    if y + 2 < 5 and findP(places[answer_i], x, y, 0, 2):
                        current_answer = 0
                        break
        answer.append(current_answer)
    return answer
