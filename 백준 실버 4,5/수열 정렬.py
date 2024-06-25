n = int(input())
a = list(map(int,input().split()))
sorted_a = sorted(a,reverse = False)

p = []
for i in range(n):
    p.append(sorted_a.index(a[i]))
    sorted_a[sorted_a.index(a[i])] = -1

for i in range(n):
    print(p[i],end = ' ')