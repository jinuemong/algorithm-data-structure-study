
# 성 지키기

n,m = map(int,input().split())

result =0
for _ in range(n):
    if input().count('X')==0:
        result+=1
print(result)

# -> 오답 모든 열 탐색이 빠짐




