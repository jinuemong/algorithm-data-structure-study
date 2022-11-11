T = int(input())
for t in range(1,T+1):
    n = int(input())
    isYes = False
    for i in range(1,10):
        if n%i==0:
            j = n//i
            if j*i==n and (0<j<10):
                isYes = True
                break
    if isYes:
        print(f"#{t}", "Yes")
    else:
        print(f"#{t}","No")

# 출처 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXkcWgFa8sADFAS8&categoryId=AXkcWgFa8sADFAS8&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2
# 풀이  :  https://jinudmjournal.tistory.com/36