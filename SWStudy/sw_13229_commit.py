T = int(input())

s_list = [0,"SAT","FRI","THU","WED","TUE","MON","SUN"]
for t in range(1,T+1):
    s = input()
    print(f"#{t}",s_list.index(s))

#문제 출처 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AX0SaDW6L2oDFASs&categoryId=AX0SaDW6L2oDFASs&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2
#문제 풀이 : https://jinudmjournal.tistory.com/27