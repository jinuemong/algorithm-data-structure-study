# 시간 초과
def solution(n, k, cmd):
    answer = 'X'*n
    del_n = []
    c_i = k  # current index

    list_n = [i for i in range(n)]

    for c in cmd:
        if c[0] == 'D':
            c_i += int(c[2])

        if c[0] == 'C':
            list_n.pop(list_n.index(c_i))
            del_n.append(c_i)
            if c_i == len(list_n):
                c_i -= 1

        if c[0] == 'U':
            c_i -= int(c[2])

        if c[0] == 'Z':
            t = del_n.pop()
            list_n.append(t)
            list_n.sort()
            if int(t) < c_i:
                c_i += 1
    for n in list_n:
        answer = answer[:n]+"O"+answer[n+1:]
    return answer

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n,k,cmd))