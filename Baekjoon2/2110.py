
# 공유기 설치

# N max : 200,000, X max : 1,000,000,000
# 이진 탐색 -> O(NlogX)
# 가장 인접한 두 공유기 사이의 최대 Gap을 이진 탐색으로 찾기

n, c = list(map(int,input().split()))
array = [] # 집의 위치
for _ in range(n):
    array.append(int(input()))
array= sorted(array) # 이진 탐색을 위한 정렬

# 방법
# 최대 Gap, 최소 Gap 탐색
# min, max의 중간값으로 min, max 갱신 -> 반복
# min > max인 경우 종료

# 정렬 했기 때문에 가장 큰 차이는 1 - 마지막 차이
# 가장 작은 차이는 1
start = 1 # 초기 min
end = array[-1] - array[0] # 초기 max
result = 0

while (start<= end):
    mid = ( start + end) // 2 # mid : Gap (min-max 차이)
    value = array[0]
    count = 1
    for i in range(1,len(array)):
        if array[i] >= value+mid:
            value = array[i]
            count+=1

    if count >= c: # C개 이상의 공유기를 설치할 수 있는 경우
        start = mid +1
        # 공유기 설치 조건에 만족하므로 result 갱신
        result = mid
    else: # C 개 이상의 공유기 설치 불가, max(end)값 갱신 후 재탐색
        end = mid-1

print(result)
