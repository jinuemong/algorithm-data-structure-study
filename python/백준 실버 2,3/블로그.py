
non_data = "SAD"
# x일동안 가장 많이 들어온 수
# 큰 순으로 정렬
# 앞뒤로 숫자를 줄이거나 늘려가서 가장 방문자 수 최대를 만족하는 조합 구하기

n, x = list(map(int,input().split()))
x_list = list(map(int,input().split()))
max_sum = sum(x_list[0:x])
max_count = 1
current_sum = max_sum
for idx in range(1,len(x_list)-x+1):
    current_sum = current_sum - x_list[idx-1] + x_list[idx+x-1]
    if max_sum < current_sum:
        max_count = 1
        max_sum = current_sum
    elif max_sum == current_sum:
        max_count+=1

if max_sum == 0:
    print(non_data)
else:
    print(max_sum)
    print(max_count)


