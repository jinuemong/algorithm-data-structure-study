



# 숫자 변환하기
# 자연수 x를 y로 변환
# x + n , x * 2 , x * 3
# x,y가 100만까지 가능
# 최소 연산으로 x를 y로 변환
# 방정식, 숫자 계산 모두 틀림
# y까지의 리스트를 생성해서 값 추측
# 연산후 작은 값으로 바꿔주면서 탐색을 진행하면
# 마지막인 y에는 최소 수가 저장
# 모든 수는 x-y 사이에 있음
# 모든 수를 포함하게 y 인덱스를 선언한 후
# y값을 하나씩 변화, 여기서 더 작은 연산의 값으로 데이터 변환
# 최종적으로는 가장 적은 연산으로 만들어진 y를 얻음

def solution(x, y, n):
    dp= [1000000 for _ in range(y+1)] # 최대 값으로 초기화
    dp[x] = 0 # 초기 count = 0
    for i in range(x,y+1):
        if i+n <= y:
            dp[i+n] = min(dp[i+n],dp[i]+1)
        if i*2 <= y:
            dp[i*2] = min(dp[i*2],dp[i]+1)
        if i*3 <= y:
            dp[i*3] = min(dp[i*3],dp[i]+1)
    if dp[y]==1000000:
        return -1
    else:
        return dp[y]


print(solution(10,40,30))