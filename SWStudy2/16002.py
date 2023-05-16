
# 16002 합성수 방정식

# 합성수 : 1과 자기 자신 이외의 다른 자연수들의 곱으로 나타낼 수 있는 자연수
# x - y = n 을 만족하는 합성수를 찾아야 하므로
# y , n+y 모두 합성수인 경우를 탐색해야 한다
import math
t= int(input())


def find_data(data):
    i = 2
    while i < data:
        if data % i == 0:
            return True
        i += 1
    return False

for t_i in range(t):
    x,y = 0,2
    n = int(input())
    while True:
        if find_data(y) and find_data(y+n):
            x = y+n
            break
        y+=1

    print(f"#{t_i+1} {x} {y}")


