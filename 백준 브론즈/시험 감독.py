n = int(input())

a = list(map(int,input().split()))

b,c= map(int,input().split())
count = 0
for i in range(len(a)):
    a[i] -= b
    count+=1
    if a[i]>0:
        count+= a[i]//c
        if a[i]%c >0:
            count+=1

print(count)