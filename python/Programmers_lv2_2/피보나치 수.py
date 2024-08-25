

# 피보나치 수
# F(0) = 0 , F(1) = 1
# F(n) = F(n-1) + F(n-2)

def solution(n):
    n_list = [0 for _ in range(n+1)]
    n_list[1] = 1
    for i in range(2,n+1):
        n_list[i] = n_list[i-1]+n_list[i-2]
    return n_list[-1] % 1234567

print(solution(5))