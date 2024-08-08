

n,m = map(int,input().split())
h_list = list(map(int,input().split()))
start,end = 1, max(h_list)

while start <= end:
    mid = (start+end) //2

    k = 0
    for h in h_list:
        if h >= mid:
            k += h - mid

    if k >=m:
        start = mid +1
    else:
        end = mid -1
print(end)