T = int(input())
prt_list = [] #출력 리스트
for t in range(1,T+1):
    a, b, c, d = map(int,input().split())
    answer = min(b,d)-max(a,c)
    if answer<0:
        answer=0
    prt_list.append(f"#{t} {answer}")

for p in prt_list:
    print(p)

# 출처 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXuUo_Tqs9kDFARa&categoryId=AXuUo_Tqs9kDFARa&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2
# 문제 풀이 : https://jinudmjournal.tistory.com/34