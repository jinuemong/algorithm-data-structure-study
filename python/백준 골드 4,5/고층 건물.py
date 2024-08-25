

# 고층 건물

# 직선의 방정식
# 해당 직선을 지나면 false
# 지나지 않으면 true 반환
# false가 온 시점엔 탐색 종려 -> 볼 수 없음
# 사이의 모든 점을 탐색하면 count +1 -> true 유지 상태면

def line_fun(x1,y1,x2,y2,a,b):
    if int((y2-y1)/(x2-x1)*(a-x1) + y1 - b) == 0: return False
    else: return True


n = int(input())
n_list = list(map(int,input().split()))
n_list = [[x+1,y] for x,y in enumerate(n_list)]
answer = 0
for a in range(len(n_list)):
    count = 0
    for b in range(len(n_list)):
        if a!=b: # 자신이 아닌 경우
            isTrue = True
            for d in range(a+1,b):
                isTrue = line_fun(n_list[a][0],n_list[a][1],n_list[b][0],n_list[b][1],n_list[d][0],n_list[d][1])
                print(isTrue)
            if isTrue: count+=1 # 사이 값이 없다
    answer = max(answer,count)
print(answer)

