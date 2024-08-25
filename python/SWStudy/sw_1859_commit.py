
T = int(input())

for t in range(1, T + 1):
    total_cost = 0
    cost, cost_count ,max = 0, 0 , 0
    n = int(input())
    n_list = list(map(int, input().split()))
    for i in range(n-1,-1,-1):
        if max<n_list[i]:
            total_cost+= (max*cost_count-cost)
            cost, cost_count = 0, 0
            max = n_list[i]
        else:
            cost+=n_list[i]
            cost_count+=1

    total_cost += (max*cost_count-cost)

    print(f"#{t}", total_cost)

# 출처 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

# 문제풀이 리뷰 : https://jinudmjournal.tistory.com/22