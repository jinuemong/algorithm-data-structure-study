import math

# 연속 인덱스를 가지는 소수
n = int(input())
ary = [True for _ in range(n+2)]

for i in range(2,int(math.sqrt(n))+1):
    if ary[i] == True:
        j = 2
        while i*j <= n:
            ary[i*j] = False
            j+=1
result = 0
for i in range(2,len(ary)):
    if ary[i]:
        count ,j= i , i+1
        while count < n:
            if ary[j]:
                count+=j
            j+=1
        if count == n:
            result+=1
print(result)