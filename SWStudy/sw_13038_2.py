tc = int(input())

for t in range(1,tc+1):
    n = int(input())
    count = n * 7  # 일주일에 꼭 한 수업은 있으니 최대 n*7만큼 출석
    a_list = list(map(int, input().split())) #수업 리스트
    a_count = a_list.count(1) #총 1의 갯수

    for a_i in range(0,len(a_list)):
        if a_list[a_i]==1:
            total_day , total_n = 0,0 #총 날짜, 총 출석
            # 이번주
            for a_i_i in range(a_i,len(a_list)):
                if a_list[a_i_i]==1:
                    total_n+=1
                total_day+=1
                if total_n==n: #이번주에 달성
                    break
            if total_n==n:
                if count>total_day:
                    count=total_day
                    continue
            # 긴 주 자르기 n-total_n은  앞 과정에서 남은 일수
            # 주 단위로 자르므로 a_count 보다 커야함
            if (n-total_n)>a_count:
                total_day+=int((n-total_n)/a_count)*7
                total_n +=int((n-total_n)/a_count)*a_count

            #중간 정검
            if total_n==n:
                if count>total_day:
                    count=total_day
                    continue
            # 마무리
            a_i_i = 0
            while total_n<n:
                if a_i_i==7:
                    a_i_i=0
                if a_list[a_i_i]==1:
                    total_n += 1
                total_day += 1

                if total_n==n:
                    if count>total_day:
                        count=total_day
                        break
                a_i_i+=1

    print(f"#{t}", count)