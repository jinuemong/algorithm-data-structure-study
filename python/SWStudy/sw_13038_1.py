tc = int(input())

for t in range(1,tc+1):
    n = int(input())
    count =n*7 #일주일에 꼭 한 수업은 있으니 최대 n*7만큼 출석
    a_list = list(map(int,input().split()))
    a_count = a_list.count(1)
    for a_i in range(len(a_list)):
        if a_list[a_i]==1:
            total,total_count = 0 , 0

            if a_count<n:
                total += int(n / a_count) * 7
                total_count=a_count*7
            #total은 총 일 수
            #total_count는 남은 n일 수
            a_i_reset = a_i
            while total_count<n:

                if a_i_reset==7:
                    a_i_reset = 0

                if a_list[a_i_reset]==1:
                    total_count+=1
                total+=1
                a_i_reset+=1
            if total<count:
                count = total

    print(f"#{t}",count)

