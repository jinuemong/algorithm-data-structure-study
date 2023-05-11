
# 평범한 베낭

# n개의 물건은 W 무게, V 가치를 가짐
# 베낭에 해당 물건을 넣어서 가면 V만큼 즐김
# 최대 K만큼의 무게의 베낭
# O(NK)의 시간 복잡도

import sys

n ,k  = map(int,input().split())

result = [[0]*(k+1) for _ in range(n+1)]
# K*N의 배열을 만들어서 각 무게를 적립해서 더함

for n_i in range(1,n+1):
    w, v = map(int,input().split())

    for k_i in range(1,k+1):
        if k_i < w:
            #무게보다 낮을 때는 이전 단계의 가치를 부여
            result[n_i][k_i] = result[n_i-1][k_i]
        else:
            # 무게보다 높거나 같으면 이전 가치와 이전 가치의 무게를 뺀 만큼의
            # 가치중 더 큰 것을 탐색
            result[n_i][k_i] = max(result[n_i-1][k_i]
                                   ,result[n_i-1][k_i-w] + v)
print(result[n][k])


