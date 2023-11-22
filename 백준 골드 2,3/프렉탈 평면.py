

# 프렉탈 평면

# 단위 시간 1 마다 n*n 개의 정사각형으로 나누어짐
# 나누어진 정사각형이 흰색이라면 가운데 k*k는 검정색으로 채워짐
# n과 k는 같은 홀짝



# s(0) = 0
# s(1) = n*n 정사각형 내부에 k*k 정사각형

s,n,k,r1,r2,c1,c2 = list(map(int,input().split()))

square = [[0]*(n) for _ in range(n)]


for i in range(s):
    if i>0:
        for i in range(len(square)): square[i] = square[i] * n
        square = list(map(list, zip(*square)))
        for j in range(len(square)): square[j] = square[j] * n
        k *= n
        n *= n

    for i in range((n-k)//2 , (n-k)//2+k):
        for j in range((n-k)//2 , (n-k)//2+k):
            square[i][j] = 1

if s==0:
    print(0)
else:
    for j in range(r1,r2+1):
        for i in range(c1, c2 + 1):
            print(square[i][j], end="")
        print()
