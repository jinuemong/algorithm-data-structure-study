T = int(input())

for t in range(1, T + 1):
    is_possible = False

    n = int(input())
    if n < 10:
        print(f"#{t}", "impossible")
        continue
    n_set = {}
    for s in list(str(n)):
        if s in n_set:
            n_set[s] += 1
        else:
            n_set[s] = 1
    n_2 = n
    while len(str(n_2)) == len(str(n)):
        # 자리수가 같은 경우 , is_possible = True 경우
        n_set_reset = n_set
        n_2 = n_2 + n
        for n_2_ in list(str(n_2)):
            if n_2_ in n_set:
                n_set_reset[n_2_] -= 1
        n_i_sum = 0
        for n_i in n_set_reset.values():
            if n_i==0:
                n_i_sum+=1
        if n_i_sum==len(str(n_2)):
            is_possible = True
        # 모든 값이 0이어야 일치


    if is_possible:
        print(f"#{t}", "possible")
    else:
        print(f"#{t}", "impossible")
