

# 골드 5

n = int(input())
n_list = list(map(int,input().split()))
min_list = []
if n ==1:
    print(-max(n_list)+sum(n_list))
else:
    min_list.append(min(n_list[0],n_list[5]))
    min_list.append(min(n_list[1], n_list[4]))
    min_list.append(min(n_list[2], n_list[3]))
    min_list.sort()

    sum_1 = (4* (n-2) * (n-1) + (n-2)**2) * (min_list[0])
    sum_2 = (4 * (n-1) + 4 * (n-2)) * (sum(min_list[:2]))
    sum_3 = 4 * (sum(min_list))
    print(sum_1+sum_2+sum_3)