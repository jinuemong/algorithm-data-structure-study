# 가장 긴 증가하는 부분 수열

n = int(input())
n_list = list(map(int, input().split()))
result = [1]*n # 모든 길이

for i in range(1,n):
    for j in range(0,i):
        if n_list[j] < n_list[i]:
            result[i] = max(result[i],result[j]+1)
print(max(result))