

# XOR 2차원 배열
# 01
# 10 을 예시로
# [0,0] -> 0 ( 1,1 or 0,0)
# [0,1] -> 1 ( 1,0 or 0,1)
# [1,0] -> 1 ( 1,0 or 0,1)
# [1,1] -> 0 ( 1,1 or 0,0)
# a0 (+) b0 -> 
for t in range(int(input())):
    n,m = map(int,input().split())
    result = "no"

    print(f"#{t+1} {result}")


