

# 수열의 합
# 가장 작은 L을 구해야 하므로, 최대값 부터 검사
# n -1 하면서->
# 추가 :  합이 n을 넘지 않을 경우
# 삭제 : 합이 n을 넘은 경우 (먼저 들어온 것부터 삭제)
# 길이가 l과 같고 합이 n이다 -> 종료

# -> 시간초과
# -> 수학적 접근
n, l = list(map(int,input().split()))

for i in range(l,101):
    x = n - (i*(i+1)/2)

    if x % i == 0:
        x = int(x/i)

        if x>=-1:
            for j in range(1,i+1):
                print(x+j,end = ' ')
            print()
            break
else:
    print(-1)
