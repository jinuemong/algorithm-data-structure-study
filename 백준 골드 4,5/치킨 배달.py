# 0 - 빈집
# 1 - 집
# 2 - 치킨

# 각 집별로 가장 가까운 치킨 거리를 구하라

# 치킨 집 중에 최대 m개를 고르고 나머지를 폐업
# 치킨 거리를 가장 작게 하려면 각 도시에서 치킨으로 가는 거리의 합이 가장 적어야 함

# 모든 도시 -> 치킨 거리를 구하기
# 각 도시의 가장 작은 치킨 거리 저장
# 정렬하여 치킨거리 리스트[:m]만큼의 합을 구함

from itertools import combinations

n, m = map(int, input().split())
chicken = []
homes = []

# 집과 치킨집 위치 저장
for j in range(n):
    for idx, value in enumerate(list(map(int, input().split()))):
        if value == 1:
            homes.append((idx, j))
        elif value == 2:
            chicken.append((idx, j))

# 각 치킨집과 집 사이의 거리 계산
result = [[0]*len(homes) for _ in range(len(chicken))]
for i, (x, y) in enumerate(chicken):
    for j, (dx, dy) in enumerate(homes):
        result[i][j] = abs(dx - x) + abs(dy - y)

# 치킨집 중에서 M개를 선택하는 모든 조합 생성
combs = combinations(range(len(chicken)), m)

# 최소 치킨 거리 초기화
min_distance = float('inf')

# 각 조합에 대해 도시의 치킨 거리 계산하여 최소값 갱신
for comb in combs:
    total_distance = 0
    for j in range(len(homes)):
        min_dist_to_home = float('inf')
        for i in comb:
            min_dist_to_home = min(min_dist_to_home, result[i][j])
        total_distance += min_dist_to_home
    min_distance = min(min_distance, total_distance)

print(min_distance)