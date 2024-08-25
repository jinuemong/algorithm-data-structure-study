c = int(input())
for num in range(1, c + 1):
    s = input()
    count=1
    for i in range(0,len(s)-1):
        if i==0 and ord(s[i])!=97:
            count=0
            break

        if ord(s[i])==97:
            count+=1
        elif ord(s[i])+1 ==ord(s[i+1]):
            count+=1
        else:
            break
    if 'a' not in s:
        print("#" + str(num), 0)
    else:
        print("#" + str(num), count)

# 출처 SW Expert Academy
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYLnMQT6vPADFATf

#문제 해결 방식
# https://jinudmjournal.tistory.com/4