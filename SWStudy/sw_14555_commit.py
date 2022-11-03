T = int(input())
for n in range(1,T+1):
    count = 0
    correct_Set = {"(|", "()", "|)"}
    st = input()
    for i in range(len(st)-1):
        if (st[i]+st[i+1]) in correct_Set:
            count+=1
    print("#"+str(n),count)


# 출처
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYGtoa3qARcDFARC&categoryId=AYGtoa3qARcDFARC&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

# 문제풀이
# https://jinudmjournal.tistory.com/10