tc = int(input())

for t in range(1,tc+1):
    n = int(input())
    n_list = list(map(int,input().split()))
    count = n*7
    n_count = n_list.count(1) #한 주의 일 수

    for day in n_list:
        total_day, total_n, n_i = 0, 0, day

        while total_n <= n:
            if total_day > count:
                break
            if n_list[n_i] == 1:
                total_n += 1
            total_day += 1

            if total_n == n:
                if count > total_day:
                    count = total_day
                    break
            n_i += 1
            if n_i == 7:
                n_i = 0

    print(f"#{t}",count)

# 출처 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXxNn6GaPW4DFASZ&categoryId=AXxNn6GaPW4DFASZ&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2
# 문제 풀이 : https://jinudmjournal.tistory.com/33