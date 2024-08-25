T = int(input())

for t in range(1, T + 1):
    n = int(input())
    is_possible = False
    if len(str(n))==1: # 1의 자리는 불가능
        print(f"#{t}", "impossible")
        continue

    n_set = {} # n의 구성 요소를 분해 후 저장

    for s in list(str(n)):
        if s in n_set:
            n_set[s]+=1
        else:
            n_set[s]= 1

    kn = n #n 보다 큰 n의 배수

    while len(str(kn))==len(str(n)):
        #자리수가 같은 경우만 탐색
        n_set_reset = n_set.copy()
        n_set_reset_count = 0
        kn = kn + n #n의 배수
        for kn_i in list(str(kn)):
            if kn_i in n_set_reset:
                if n_set_reset[kn_i]>0:
                    n_set_reset[kn_i]-=1
                    n_set_reset_count+=1
                #값을 찾으면 자리를 채움 , count +1

        if n_set_reset_count == len(str(kn)):
            is_possible = True
            break

    if is_possible:
        print(f"#{t}", "possible")
    else:
        print(f"#{t}", "impossible")

# 출처 : https://swexpertacademy.com/main/code/problem/problemDetail.do

# 개인 문제 풀이 : https://jinudmjournal.tistory.com/17