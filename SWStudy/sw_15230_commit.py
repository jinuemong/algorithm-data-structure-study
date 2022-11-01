max_st = "abcdefghijklmnopqrstuvwxyz"
T = int(input())
for num in range(1,T+1):
    st = input()
    count = 0
    for i in range(0,len(st)): #문자 하나씩
        if st[i] == max_st[i]:
            count+=1
        else:
            break
    print("#"+str(num),count)

# 출처 SW Expert Academy
#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYLnMQT6vPADFATf