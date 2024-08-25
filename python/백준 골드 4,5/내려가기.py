# 0번 위치 -> 0,1
# 1번 위치 -> 0,1,2
# 2번 위치 -> 1,2
# 이전 state를 저장하고, 매번 최적의 선택을 한다
# min, max 따로 트리를 탄다
# 다음의 0번 -> (0,1번에서 온다) -> min,max 선택
# 다음의 1번 -> (0,1 or 1,2번에서 온다) -> min, max 선택
# 다음의 2번 -> (1,2번에서 온다) -> min,max 선택
# 최종 결과 선택
import sys

input = sys.stdin.read

data = input().split()
n = int(data[0])
idx = 1

current_min = [0] * 3
current_max = [0] * 3

current_min[:] = list(map(int, data[1:4]))
current_max[:] = list(map(int, data[1:4]))
idx += 3

for i in range(1, n):
    a, b, c = map(int, input().split())
    idx += 3

    # 현재 값 계산을 위한 이전 단계 저장
    previous_min = current_min[:]
    previous_max = current_max[:]

    # 갱신
    current_min[0] = min(previous_min[0], previous_min[1]) + a
    current_min[1] = min(previous_min[0], previous_min[1], previous_min[2]) + b
    current_min[2] = min(previous_min[1], previous_min[2]) + c

    current_max[0] = max(previous_max[0], previous_max[1]) + a
    current_max[1] = max(previous_max[0], previous_max[1], previous_max[2]) + b
    current_max[2] = max(previous_max[1], previous_max[2]) + c

# 결과 출력
print(max(current_max), min(current_min))