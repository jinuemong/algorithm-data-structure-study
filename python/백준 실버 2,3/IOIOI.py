n = int(input())
m = int(input())
s = input()
cursor,count,result = 0,0,0
while cursor < (m -1) :
    if s[cursor : cursor + 3] == "IOI": ## 발견 시 count +=1
        count +=1
        cursor += 2 # IOI의 I부터 재 탐색
        if count == n: # count == n일 경우 탐색 완료
            result += 1
            count -= 1
    else:
        cursor += 1 # 미 탐색 시 cursor +1
        count = 0 # 초기화
print(result)