
T= int(input())

for t in range(1,T+1):
    total_cost = 0
    cost , cost_count = 0, 0
    n = int(input())
    n_list = list(map(int,input().split()))
    for i in range(n):

        max_num = max(n_list[i:n+1])
        if n_list[i]==max_num:
            total_cost+= (max_num*cost_count-cost)
            cost, cost_count = 0,0
        else:
            cost+=n_list[i]
            cost_count+=1

    print(f"#{t}",total_cost)

#제한 시간 초과