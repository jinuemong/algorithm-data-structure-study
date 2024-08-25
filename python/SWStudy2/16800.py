

# 구구단 걷기

# i,j 셀에는 정수 i*j가 있다
# 오른쪽이나 아래쪽으로 이동 가능
# i+1,j or i,j+1로 이동
# 정수 n이 주어질 때 n에 적혀있는 셀에 도착하기 위한 최소 이동 거리
# 현재 위치는 (1,1)
# 약수를 구해서 가장 작은 값을 가지는 약수 조합을 찾음
# 두 수의 합이 답
import math
t = int(input())

# ex 1~10이라고 하면
# 1, 2,5 , 10에서 5까지, n에 루트 씌운 값 + 1만큼 탐색
for t_i in range(t):
    n = int(input())
    result = 10000000000001
    for i in range(1,int(math.sqrt(n)+1)):
        if n%i==0:
            t = int(n/i)
            new_result = t+i -2
            if result>new_result:
                result = new_result
    print(f"#{t_i+1} {result}")