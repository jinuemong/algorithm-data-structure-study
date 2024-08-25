
# 0 1 2
# 0번 1번, 1번 2번은 서로 색이 달라야 함
# 1번 집은 0번, 2번과 색이 달라야 함

# ex 빨 - 초 - 파
#       - 파 - 초
# 첫 번째 빨빨 초초 파파 (6가지 )
# 두 번째 파초 빨파 빨초  (6가지)
# 세 번째 초파 파빨 초빨 ( 6가지 )
# 00 11 22 rr gg bb
# 12 02 01 gb rb rg
# 21 20 10 gb br gr
# 00 11 22 rr gg bb
# 규칙 3  * 6 * 6 * 6 ..... (재귀 ? )

n = int(input())
a = [0] * n

for i in range(n):
    a[i] = list(map(int, input().split()))
for i in range(1, n):
    a[i][0] = min(a[i - 1][1], a[i - 1][2]) + a[i][0]
    a[i][1] = min(a[i - 1][0], a[i - 1][2]) + a[i][1]
    a[i][2] = min(a[i - 1][0], a[i - 1][1]) + a[i][2]

print(min(a[n - 1][0], a[n - 1][1], a[n - 1][2]))