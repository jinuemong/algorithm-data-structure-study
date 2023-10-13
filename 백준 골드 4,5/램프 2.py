

# 한 행을 가득 채울 수 있는 k번을 적용
# -> 적용이 가능 할 경우 다른 k를 적용시킨 행 켜줌
# 행의 개수를 카운트해서 가장 많은 경우의 수 구함

n,m = list(map(int,input().split()))
lamp = []
for _ in range(n):
    lamp.append(list(map(int,list(input()))))

k = int(input())
max_data = 0

for col in range(n):
    zero_count = 0
    for num in lamp[col]:
        if num == 0:
            zero_count+=1

    col_count = 0
    if zero_count <= k and zero_count%2 == k%2: # 같은 수 (홀, 짝)
        for col2 in range(n):

            if lamp[col] == lamp[col2]:
                col_count+=1
    max_data = max(col_count,max_data)
print(max_data)