#출처 : https://www.acmicpc.net/problem/1966
# 문제 풀이
T = int(input())

for _ in range(T):
    n, m = map(int,input().split())
    n_list = list(map(int,input().split()))
    n_list = [(i,index) for index,i in enumerate(n_list)]
    # enumerate : index: i로 분리
    m_count = 0
    max_num = max(n_list,key=lambda x:x[0])[0]
    # x[0]를 기준으로 큰 값을 뽑은 후의 값 [0]
    while True:
        if n_list[0][0]==max_num:
            m_count+=1
            if n_list[0][1]==m:
                print(m_count)
                break
            else:
                n_list.pop()
                max_num = max(n_list, key=lambda x: x[0])[0]
        else:
            n_list.append(n_list.pop())
