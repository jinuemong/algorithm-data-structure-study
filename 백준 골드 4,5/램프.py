

n,m = list(map(int,input().split()))
lamp = []

for i in range(n):
    lamp.append(list(map(int,list(input()))))

k = int(input())
max_data = 0

for i in range(n):
    current = 0
    for j in range(m):
        if k%2==1:
            if lamp[i][j]==0: lamp[i][j]= 1
            else: lamp[i][j] = 0
        current+=lamp[i][j]
    max_data = max(current,max_data)
print(max_data)