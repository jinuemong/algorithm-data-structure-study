n, k, p, x = map(int, input().split())

# n : 1~ n까지 수로 변환
# k : 자리수 (5의 2자리 수 -> 05
# p : 1~p 개의 LED 반전
# x : 현재 층 수

numbers = [
    "1110111",
    "0010001",
    "0111110",
    "0111011",
    "1011001",
    "1101011",
    "1101111",
    "0110001",
    "1111111",
    "1111011"
]

x_number = [numbers[int(i)] for i in str(x).zfill(k)]
result = 0

for n in range(1, n+1):
    current_number = [numbers[int(i)] for i in str(n).zfill(k)]
    cnt = 0
    for x, c in zip(x_number, current_number):
        for i, j in zip(x, c):
            if i != j:
                cnt += 1
            if cnt > p: break

    if 1 <= cnt <= p:
        result += 1
print(result)
