
# 햄버거 분배

n,k = map(int,input().split())
n_list = list(input())
result = 0
for idx in range(n):
    if n_list[idx] == "P":
        for i in range(max(idx-k,0), min(idx+k+1,n)):
            if n_list[i] == "H":
                n_list[i] = 0
                result+=1
                break

print(result)