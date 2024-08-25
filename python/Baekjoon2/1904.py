

# 동적 프로그래밍

# 규칙 찾기
# n = 1  1 (1)
# n = 2  00, 11 (2)
# n = 3  100 , 001, 111 (3)
# n = 4  0011, 0000, 1001, 1100, 1111 (5)

# n(3) = n(1)+n(2)
# n(4) = n(2) + n(3) 규칙
import sys
n = int(sys.stdin.readline())

start = 1
mid = 1

for i in range(2,n+1):
    next = (start + mid)%15746
    start = mid
    mid = next
print(mid)