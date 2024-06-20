n,k = map(int,input().split())
nk = list(map(int,input().split()))
counter = [0] * (max(nk) + 1)
left, right = 0,0
answer = 0
while right < n:
    if counter[nk[right]] < k:
        counter[nk[right]]+=1
        right +=1
    else:
        counter[nk[left]] -=1
        left +=1
    answer = max(answer,right - left)
print(answer)
