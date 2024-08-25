def solution(park, routes):
    answer = find_S(park)

    for route in routes:
        op, n = route.split()
        n = int(n)
        if op == "N":
            if find_op(answer[0] - n, len(park)) and find_X(
                    ''.join(list(zip(*(park)))[answer[1]][answer[0] - n:answer[0]])):
                answer[0] -= n
        elif op == "S":
            if find_op(answer[0] + n, len(park)) and find_X(
                    ''.join(list(zip(*(park)))[answer[1]][answer[0]:answer[0] + n + 1])):
                answer[0] += n
        elif op == "W":
            if find_op(answer[1] - n, len(park[0])) and find_X(park[answer[0]][answer[1] - n:answer[1]]):
                answer[1] -= n
        elif op == "E":
            if find_op(answer[1] + n, len(park[0])) and find_X(park[answer[0]][answer[1]:answer[1] + n + 1]):
                answer[1] += n

    return answer


def find_op(n, d):
    if 0 <= n < d:
        return True
    else:
        return False


def find_X(data_set):
    x = data_set.find("X")
    if data_set.find("X") == -1:
        return True
    else:
        return False

def find_S(data_set):
    for i in range(len(data_set)):
        for j in range(len(data_set[0])):
            if data_set[i][j] == "S":
                return  [i,j]

park , routes = ["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"]
print(solution(park, routes))
