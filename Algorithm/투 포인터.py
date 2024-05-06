# 두 포인터를 사용하여 문자열이나 정렬 된 배열에서 원하는 값을 찾거나 구간합을 구함
# 슬라이딩 윈도우와 유사하나, 고정 된 구간이 아닌 가변적인 구간을 탐색

array = [1, 2, 3, 4, 5, 6]
array.sort()

start, end = 0, len(array) - 1
target = 6

while start < end:
    s = array[start] + array[end]
    if s > target:
        end -= 1
    elif s < target:
        start += 1
    else:
        print(start, end)
        start += 1
        end -= 1