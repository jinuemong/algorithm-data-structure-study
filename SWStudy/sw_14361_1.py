def listToInt(st):
    result = ""
    for s in st:
        result+=s+''

    return int(result.strip())

T = int(input())

for t in range(1,T+1):
    is_possible = False
    n = int(input())
    n_list = list(str(n))

    for n_ in range(len(n_list)-1):
        for n__ in range(len(n_list)):
            des =n_list[n_]
            n_list[n_] = n_list[n__]
            n_list[n__] = des
            if listToInt(n_list)%n==0:
                is_possible=True

    if is_possible:
        print(f"#{t}","possible")
    else:
        print(f"#{t}", "impossible")