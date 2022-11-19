t = int(input())

# 사전에서 caa 다음이 cab가 아닌 , caaa임
for t in range(1,t+1):
    p,q = input().strip(), input().strip()
    if p + 'a' == q:
        print(f"#{t}","N")
    else:
        print(f"#{t}", "Y")

# 출처 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXdHwI1aCy0DFAS5&categoryId=AXdHwI1aCy0DFAS5&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=3