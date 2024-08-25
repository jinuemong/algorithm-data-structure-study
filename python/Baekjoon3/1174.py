

# 1174 줄어드는 수
# 321 ->
# 950 ->
# 위의 수는 줄어드는 수
# 322 , 958 x

# n 번재로 작은 줄어드는 수 출력

# ex 1번째 -> 0
# 2번째 -> 1
# 3번째 -> 2
# 19번재 -> 42 ....

# -> 답이 없을 경우는 -1 출력

n = int(input())
data_set = [i for i in range(10)]
def check(data):
    if len(data_set)>50000:
        return
    for i in range(int(data[-1])):
        next = data+str(i)
        data_set.append(int(next))
        check(next)

check("10")
print(data_set)


