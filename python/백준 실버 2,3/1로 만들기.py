n = int(input())
n_list = [float("inf") for _ in range(n + 1)]
n_list[n] = 0
for i in range(n, 1, -1):
    if i % 3 == 0 and n_list[i // 3] > n_list[i] + 1:
        n_list[i // 3] = n_list[i] + 1
    if i % 2 == 0  and n_list[i // 2] > n_list[i] + 1:
        n_list[i // 2] = n_list[i] + 1
    if n_list[i - 1] >= n_list[i] + 1:
        n_list[i - 1] = n_list[i] + 1
print(n_list[1])