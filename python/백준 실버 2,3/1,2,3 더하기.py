
t = int(input())
for _ in range(t):
    n = int(input())
    n_list = [0 for i in range(n+3)]
    n_list[1] , n_list[2], n_list[3]  = 1,1,1 # +1
    for i in range(1,n):
        for j in range(1,4):
            n_list[i+j] += (n_list[i])
    print(n_list[n])