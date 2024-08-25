import re

# Contact

# 입력 값 중에 가장 길이가 긴 것 보다 큰 수가 나올 때까지 반복

T = int(input())
data_list = [ input().strip() for _ in range(T)]
for data in data_list:
    p = re.compile("(100+1+|01)+")
    if p.fullmatch(data): print("YES")
    else: print("NO")
