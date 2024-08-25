
# 점화식 활용
# 1 = 1
# 2 = 2
# 3 = (1,2)(2,1)(1,1,1) 3
# 4 = (1,1,1,1)(1,2,1)(2,1,1)(1,1,2)(2,2) 5

def solution(n):
    if n <3:
        return n
    d = [0]*(n+1)
    d[1],d[2] = 1,2
    for i in range(3,n+1):
        d[i] = d[i-2]+d[i-1]
    return d[-1]%1234567

print(solution(4))