# 1 : 좌표 x,y의 가장 위의 블록을 제거하여 저장 -> 2초
# 2 : 저장 된 블록을 꺼내서 좌표 x,y의 가장 위에 있는 블록 위에 놓음 -> 1초

n, m, b = map(int, input().split())
nm_list = []
for _ in range(n):
    nm_list.append(list(map(int, input().split())))

# 땅 높이가 0 ~ 256이다,
# 주어진 높이를 채울 수 있는지 확인하면서 문제를 푼다
result = [float("inf"), 0]  # 시간, 높이 (시간은 상관 없이 높이가 가장 높은 시간 출력 )
for current in range(0, 257):
    invent_b = 0
    use_b = 0
    for i in range(n):
        for j in range(m):
            if nm_list[i][j] > current:
                invent_b += (nm_list[i][j] - current)
            else:
                use_b += (current - nm_list[i][j])
    if use_b > invent_b + b:
        continue
    new_result = invent_b * 2 + use_b
    if result[0] > new_result:
        result[0], result[1] = new_result, current
    elif result[0] == new_result:
        result[1] = max(result[1],current)
print(result[0],result[1])
