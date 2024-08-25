

# 가로등 개수 m , 위치 x
# 최소한의 높이로 굴다리 모든 길을 밝히려 함
# 모든 가로등은 크기가 같아야 함
# 가로등의 높이만큼 왼, 오로 h만큼 비춤
# ex 가로등의 높이 1 = 3칸
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

# 방법 -> 0과 첫 가로등 사이, 마지막 가로등과 n 사이, 최대 가로등 사이의 거리 구해서 비교

n_list = list(map(int,input().split()))
data_set = [n_list[0],(n-n_list[-1])]

if len(n_list)>1:
    for i in range(1,len(n_list)):
        result = n_list[i] - n_list[i - 1]
        if result%2==0:
            data_set.append(result//2)
        else:
            data_set.append(result//2+1)

print(max(data_set))