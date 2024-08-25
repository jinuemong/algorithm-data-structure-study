
T = int(input())
def list_to_int(lst):
    result = ""
    for l in lst:
        result+=l+''
    return int(result.strip())

def tr_m_list(t, m):
    min , max = m , 0

    list_m = list(str(m))

    for i in range(len(list_m)):
        for j in range(len(list_m)):
            list_m = list(str(m))

            dest = list_m[i]
            list_m[i] = list_m[j]
            list_m[j]= dest

            if list_m[0] == '0':
                continue

            tr_m = list_to_int(list_m)
            if tr_m<min:
                min = tr_m
            if tr_m>=max:
                max = tr_m

    print(f"#{t}", min,max)

for t in range(1,T+1):
    m = int(input())
    tr_m_list(t,m)

# 문제 출처 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AX4EJPs68IkDFARe&categoryId=AX4EJPs68IkDFARe&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
# 문제 풀이 : https://jinudmjournal.tistory.com/28