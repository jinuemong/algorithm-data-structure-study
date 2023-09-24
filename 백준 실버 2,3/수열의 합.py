

# 수열의 합
# 가장 작은 L을 구해야 하므로, 최대값 부터 검사
# n -1 하면서->
# 추가 :  합이 n을 넘지 않을 경우
# 삭제 : 합이 n을 넘은 경우 (먼저 들어온 것부터 삭제)
# 길이가 l과 같고 합이 n이다 -> 종료

from collections import deque
n, l = list(map(int,input().split()))

data_list = deque([])
sum ,next, isTrue= 0,n-1,False

while next>=0 and not isTrue:
    if sum<n or l>len(data_list):
        data_list.append(next)
        sum += next
    if sum >n and len(data_list)>0:
        sum -= data_list.popleft()
    if len(data_list)>=l and sum==n:
        isTrue = True
        break
    next -= 1

if isTrue:
    for data in sorted(list(data_list)):
        print(data,end = " ")
else: print(-1)