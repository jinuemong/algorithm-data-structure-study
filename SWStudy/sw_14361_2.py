
T = int(input())

for t in range(1,T+1):
    is_possible = False

    n = int(input())
    if n<10:
        print(f"#{t}", "impossible")
        continue
    n_set = {}
    for s in list(str(n)):
        if s in n_set:
            n_set[s]+=1
        else:
            n_set[s] =1

    n_2 = n
    while len(str(n_2))==len(str(n)): #자리수가 같은 경우만
        n_set_reset = n_set
        n_2 = n_2 + n
        for n_2_ in list(str(n_2)):
            if n_2_ in n_set:
                n_set_reset[n_2_]-=1
                if n_set_reset[n_2_]<0:
                    break
            else:
                break
        is_possible = True
        break

    if is_possible:
        print(f"#{t}","possible")
    else:
        print(f"#{t}", "impossible")