

# n 진수 게임


def solution(n, t, m, p):
    data = list(''.join([ make_jinsu(i,n,"") for i in range(t*m)]))
    return ''.join([k for i,k in enumerate(data) if i % m +1 == p][:t])

def make_jinsu(num,k,data):
    of = ["A","B","C","D","E","F"]
    if num==0:
        return str(num)
    while num>0:
        if len(str(num%k)) > 1:
            data = of[num%k-10] + data
        else:
            data=str(num%k) + data

        num = num//k
    return data
n = 2
t = 4
m = 2
p = 1

print(solution(n,t,m,p))