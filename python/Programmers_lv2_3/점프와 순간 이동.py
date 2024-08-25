

# 점프와 순간 이동

# 2가지 기능 : k 칸 앞으로 점프 (k 만큼의 건전지), 현재 온거리 * 2 (0 만큼의 건전지)
# 순간이동이 더 효율적
# 거리 n이 주어질 경우 건저지 최소 값 구하기
# n이 상당히 큰 수 -> 완전 탐색은 어려움
# 처음 위치는 0이므로 무조건 1번의 건전지 사용을 해야한다
# 거리 : n - 1 , k = 1

def solution(n):
    ans,k = 0, 0

    while ans<n:
        print("f3",ans,k)
        if 0< ans *2 <= n and not (ans+1)*2==n:
            ans*=2
        else:
            ans+=1
            k+=1



    return k

print(solution(5000))