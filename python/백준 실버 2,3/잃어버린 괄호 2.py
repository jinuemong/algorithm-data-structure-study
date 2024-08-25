
# 다시 풀기
# 55-50+40 에서
# 55 -(50+40) 샏각하기
# -미리 적용하면 안됨

s = input().strip().split('-')
temp = []

for i in s:
    cnt = 0
    for j in i.split('+'):
        cnt += int(j)
    temp.append(cnt)

result = temp[0]
for i in temp[1:]:
    result -= i
print(result)