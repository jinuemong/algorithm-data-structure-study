

# 카펫
# 결국에는 가로 * 세로는 전체 블럭의 수 ( 블랙 + 옐로 )
# 가로 길이가 더 길거나 같으므로,
# 루트 n 까지의 수 중에서 가장 큰 수를 역으로 출력

from math import sqrt
def solution(brown, yellow):
    answer,data = [],brown+yellow
    for i in range(int(sqrt(data))+1,0,-1):
        if data%i == 0 and yellow == data - (2*(i)+2*(data//i)-4):
            return sorted([i,data//i],reverse=True)


print(solution(24,24))