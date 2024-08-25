

# n*m의 직사각형에서 가장 큰 정사각형의 넓이 구하기
# 행 또는 열이 평행해야 하므로, 마름모 정사각형은 불가능

import sys; input = sys.stdin.readline

n,m = list(map(int,input().split()))
n_list = [list(map(int,list(input().strip()))) for _ in range(n)]
result = 1
for i in range(len(n_list)):
    for j in range(len(n_list[0])):
        x,y = i,j
        while x<len(n_list) and y<len(n_list[0]):
            if n_list[i][j]==n_list[x][j]==n_list[i][y]==n_list[x][y]:
                result = max(result,x-i+1)
            x += 1; y += 1;
print(result*result)

