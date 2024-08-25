
# 기타리스트
# 시간 초과
n, s, m = map(int,input().split())

v = list(map(int,input().split()))

max_data = -1

def play(data,i):
    global max_data
    if data <0 or data>m:
        return
    i += 1
    if i == len(v):
        max_data = max(max_data,data)
        return
    play(data-v[i],i)
    play(data+v[i],i)

play(s-v[0],0)
play(s+v[0],0)

print(max_data)


