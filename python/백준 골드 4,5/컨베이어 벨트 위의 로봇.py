from collections import deque
n, k = map(int,input().split())
a = deque(list(map(int,input().split()))) # 내구도
belt = deque([False] * n)
# 이동하는 칸에 로봇이 없고, 그 칸 내구도가 1 이상 남아있어야 한다  (이동 조건)
# 이동할 수 없다면 가만히 있는다
# 올리는 위치의 칸의 내구도가 0이 아니라면 올리는 위치에 로봇을 올린다
# 내구도가 0인 칸의 개수가 k개 이상이라면 과정을 종료
# 그렇지 않다면 반복
# 1 ~ 2n-1 번칸까지 이동 (다음 칸 번호로)
# 2n 칸은 1번 칸의 위치로 이동
# n번빼로 이동한다면, 자동으로 n+1로 이동
# 올리는 위치에 올리거나, 어떤 칸으로 이동하면 내구도 1 감소

# 3 (n), 2 (종료 조건 -> 내구도가 0인 칸의 개수 )

# 내구도
#       1(1) 2(2) 3(1) ( 내림 )
# (올림) 6(2) 5(1) 4(2)

# n개의 que를 만들어서 이동
# 각 인덱스로 que 대체
# que에 인덱스로 접근

result = 0

while True:
    result +=1

    # 벨트가 각 칸 위에 로봇과 함께 회전
    belt.rotate(1)
    a.rotate(1)

    # 로봇 즉시 내리기
    belt[n-1] = False

    for i in range(n-2,-1,-1):
        if belt[i] and not belt[i+1] and a[i+1] > 0:
            # belt[i] : 로봇 존재
            # belt[i+1] : 다음 칸 로봇 미존재
            # 내구도 1 이상
            belt[i] , belt[i+1] = False,True # 로봇 이동
            a[i+1] -= 1 # 내구도 감소
    belt[n-1]  = False

    if a[0] > 0:
        belt[0] = True
        a[0] -= 1

    if a.count(0) >= k:
        break

print(result)