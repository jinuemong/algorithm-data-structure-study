
n,tasu,p = list(map(int,input().split()))

if n == 0:
    print(1)
else:
    score = list(map(int,input().split()))
    if n == p and score[-1] >= tasu:
        print(-1)
    else:
        res = n + 1  # 최저 등수
        for i in range(n):
            if score[i] <= tasu:
                res = i + 1
                break
        print(res)



