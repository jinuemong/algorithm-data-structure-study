T = int(input())
for n in range(1,T+1):
    is_possible = True
    i,j = map(int , input().split()) #격자판
    prev_list = [] #이전 격자

    for _ in range(0,i):
        if not is_possible:
            break

        st = list(input())[0:j] #새로운 격자

        for k in range(0,len(st)-1):
            if st[k]=="?" or st[k+1]=="?":
                continue
            if st[k]==st[k+1]:
                is_possible = False
                break
            if len(prev_list)>0:
                if st[k]=="?" or prev_list[k]=="?":
                    continue
                if st[k]==prev_list[k]:
                    is_possible = False
                    break

        prev_list = st

    if is_possible:
        print("#"+str(n),"possible")
    else:
        print("#"+str(n),"impossible")
