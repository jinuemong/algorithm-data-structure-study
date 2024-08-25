

# 16910 :원 안의 점


t = int(input())
# x ^ 2 + y ^ 2 < n ^ 2
# n이 1인 경우
# (0,0) (1,0) (0,1) (-1,0) (0,-1)
for t_i in range(t):
    n = int(input())
    result = 0
    for i in range(-n,n+1):
        for j in range(-n,n+1):
            if i*i + j*j <= n*n:
                result+=1

    print(f"#{t_i+1} {result}")