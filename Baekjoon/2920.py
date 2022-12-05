# 출처 : https://www.acmicpc.net/problem/2920

ascending, descending = True, True

k = list((map(int,input().split(' '))))

for i in range(len(k)-1):
    if k[i]+1!=k[i+1]:
        ascending = False
    if k[i]-1!=k[i+1]:
        descending = False
if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")