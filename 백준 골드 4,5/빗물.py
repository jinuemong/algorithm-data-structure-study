
h, w = map(int,input().split())

# 풀이 방식 -> 첫 높이를 저장
# 더 낮은 높이 발견 -> 높이를 카운트한다
# 같거나 높은 높이 발견 -> 카운트 된 높이를 정산한다

n_list = list(map(int,input().split()))
result = 0
prev,prev_sum = -1, 0
for n in n_list:
    print(result)
    if n < prev:
        prev_sum += (prev - n)
    else:
        result += prev_sum
        prev = n
print(result)
