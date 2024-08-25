c = int(input())
for num in range(1,c+1):
    s = input()
    count, max_count, prev_num = 0, 0, 0
    reset = True
    for a in s:
        if not reset:
            if prev_num + 1 == ord(a):
                count += 1
                prev_num = ord(a)
            else:
                if max_count < count:
                    max_count = count
                reset = True
                count = 0
                prev_num = 0

        if ord(a) == 97 and reset:
            count += 1
            prev_num = ord(a)
            reset = False
    if max_count > count:
        print("#"+str(num),max_count)
    else:
        print("#" + str(num), count)

# 출처 SW Expert Academy
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYLnMQT6vPADFATf

#문제 해결 방식
# https://jinudmjournal.tistory.com/4