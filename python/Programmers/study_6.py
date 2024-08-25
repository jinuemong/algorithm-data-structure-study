def solution(park, routes):
    answer = [0,0]
    for route in routes:
        op, n = route.split()
        n = int(n)
        if op =="N":
            if find_op(answer[0]-n,park):
                answer[0] -=n
        elif op =="S":
            if find_op(answer[0]+n,park):
                answer[0]+=n
        elif op == "W":
            if find_op(answer[1]-n,park):
                answer[1]-=n
        else:
            if find_op(answer[1]+n,park):
                answer[1]+=n

    return answer

def find_op(d , park):
    if 0<= d < len(park):
        return True
    else:
        return False


park = ["SOO","OOO","OOO"]
routes = ["E 2","S 2","W 1"]
print(solution(park,routes))