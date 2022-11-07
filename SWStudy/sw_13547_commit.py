T = int(input())

for t in range(1,T+1):
    sojeong_lose = 0
    s = input()
    for s_i in s:
        if s_i =='x':
            sojeong_lose+=1
    if sojeong_lose<8:
        print(f"#{t}","YES")
    else:
        print(f"#{t}","NO")


# 문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AX6PP9G6p1sDFAS9&categoryId=AX6PP9G6p1sDFAS9&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
# 문제풀이 : https://jinudmjournal.tistory.com/21