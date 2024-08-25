# 출처 : https://www.acmicpc.net/problem/13335
# 리뷰
from collections import deque
n, w, L = list(map(int, input().split()))
arr = deque(list(map(int,input().split())))
w_q = deque([0]*w)
count,sum,out_count = 0,0, 0
while arr or out_count<n:
    w_q.append(w_q.popleft())

    # 나가기 기능
    if w_q[-1] != 0:
        sum -= w_q[-1]
        w_q[-1] = 0
        out_count+=1

    # 새로 들어오기 가능
    if len(arr)>0 and w_q[-1]==0 and sum+arr[0]<=L:
        w_q[-1]=arr.popleft()
        sum+=w_q[-1]

    count+=1

print(count)

