

n, s, m = map(int,input().split())

v = list(map(int,input().split()))

result = [[0]*(m+1) for _ in range(n+1)] # 0~ m 까지 값 조사
result[0][s] = 1 # 첫 true

for i in range(1,n+1):
    for j in range(m+1):
        if result[i-1][j] == 0: # false
            continue
        if j - v[i-1] >=0: # -값이 0보다 큼
            result[i][j-v[i-1]] = 1 # true
        if j + v[i-1] <=m: # +값이 m보다 작거나 같음
            result[i][j+v[i-1]] = 1 # true

answer = -1
for i in range(m,-1,-1): #역순
    if result[n][i] ==1: #마지막 행의 최대값 탐색
        answer = i
        break
print(answer)