
# 트로피


def count(list):
    count ,prev_max= 0,0
    for data in list:
        if prev_max <data:
            count+=1
            prev_max=data

    return count

n_list = []
for _ in range(int(input())):
    n_list.append(int(input()))
print(count(n_list))
print(count(reversed(n_list)))
# 왼쪽 탐색 오른쪽 탐색
# 앞의 값이 뒤의 값보다 작아야 보임