t = int(input())
answer = []
def getP(r):
    return int(11-r/20)

def findR(x,y):
    r_list = [200,180,160,140,120,100,80,60,40,20]
    for r_i in range(len(r_list)):
        if x*x + y*y <= r_list[r_i]*r_list[r_i]:
            continue
        if r_i-1 <0:
            return 11
        else:
            return r_list[r_i-1]

for t in range(1,t+1):
    total = 0
    n = int(input())

    for _ in range(n):
        x,y = map(int,input().split())
        total+= getP(findR(x,y))

    answer.append(f"#{t} {total}")
for a in answer:
    print(a)



# 출처 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXZuaLsqz9wDFAST&categoryId=AXZuaLsqz9wDFAST&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=3