
n = int(input())
n_list = [list(input()) for _ in range(n)]
connected = [[0]*n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if n_list[i][j] == "Y" or (n_list[i][k]=="Y" and n_list[k][j] == "Y"):
                connected[i][j] = 1

print(max([sum(row)for row in connected]))