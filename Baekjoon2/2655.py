

# 가장 높은 탑 쌓기

n = int(input()) # n <= 100

# 밑면의 넓이, 높이, 무게

# 넓이, 무게는 같을 수 없으며 높이는 같을 수 있음
# 밑면이 좁은 벽돌 위에 밑면이 넓은 벽돌을 쌓을 수 없음
# -> 큰 수부터 작은 순으로 쌓아야 함
# 무게가 무거운 벽돌을 무게가 가벼운 벽돌 위에 쌓을 수 없음
# -> 큰 수부터 작은 순으로 쌓아야 함

# 넓이, 무게, 높이
array= []
array.append((0,0,0,0))
for i in range(1,n+1):
    w,h,k = map(int,input().split())
    array.append((i,w,h,k))

array.sort(key=lambda data : data[3])

dp = [0] * (n+1) # 동적 정렬을 위한 배열


# n의 제곱으로 알고리즘 끝내기
for i in range(1,n+1):
    for j in range(0,i):
        if array[i][1] > array[j][1]: # 너비 비교
            dp[i] = max(dp[i],dp[j] + array[i][2]) #높이 비교

max_value = max(dp)
index = n
result = [] # 순서대로 출력하기 위함

while index != 0:
    if max_value == dp[index]:
        result.append(array[index][0]) #인덱스
        # 무게를 빼줘서 다음 인덱스를 찾음
        max_value -=array[index][2]
    index -=1


# 출력 총 벽돌의 수
# 벽돌의 번호를 위 -> 아래 순으로 출력

# 가장 높은 탑을 쌓아야 하므로 w,k의 변화에 따른 h의 값중
# 제일 큰 h 값을 구해야 한다

print(len(result))
for data in reversed(result):
    print(data)
