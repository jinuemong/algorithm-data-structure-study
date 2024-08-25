# 출처 : https://www.acmicpc.net/problem/1874

n = int(input())

s_i = 1
result = []
s = []  # 스택

for i in range(1, n + 1):
    n_i = int(input())  # 탐색할 숫자

    while s_i <= n_i:  # 데이터까지
        s.append(s_i)
        s_i += 1
        result.append("+")
    if s[-1] == n_i:  # 같은 원소 발견
        s.pop()
        result.append("-")
    else:
        result = "NO"
        break

if result == "NO":
    print(result)
else:
    for i in result:
        print(i)


