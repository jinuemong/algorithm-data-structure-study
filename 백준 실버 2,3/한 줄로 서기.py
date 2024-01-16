

# 앞에서 부터 자기보다 큰 수를 카운트해서 자리 마련해주기 ?

n = int(input())
data_set = list(map(int,input().split()))
result = [0]*n

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == data_set[i] and result[j] == 0:
            result[j] = i+1
            break
        elif result[j] == 0:
            cnt+=1

# for idx, data in enumerate(data_set):
#     data_idx = data
#     while result[data_idx] != 0:
#         data_idx += 1
#     result[data_idx] = idx+1

for data in result: print(data,end=" ")