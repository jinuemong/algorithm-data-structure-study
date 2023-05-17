
n = 8
# row, col로 데이터 카운트
# 조건을 벗어나면 바로 no
for t in range(int(input())):
    result = "yes"
    col = set()  # 열 탐색
    row = set() # 행 탐색
    for i in range(n):
        st = input().strip()
        for j in range(n):
            if st[j]=='O':
                if i in col:  # 열 검사
                    result = "no"
                    break
                else:
                    col.add(i)
                if j in row: # 행 검사
                    result = "no"
                    break
                else:
                    row.add(j)

        if result=="no":
            break
    if len(col)!=8 or len(row)!=8:
        result = "no"
    print(f"#{t+1} {result}")


