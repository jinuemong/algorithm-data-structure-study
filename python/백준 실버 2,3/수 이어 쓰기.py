
# 앞에서 부터 처리
from collections import deque
n_list = deque(list(input()))
i = "1"
while n_list:
    for k in list(i):
        if len(n_list) == 0: break
        if n_list[0] == k:
            n_list.popleft()
    i = str(int(i)+1)
print(int(i)-1)