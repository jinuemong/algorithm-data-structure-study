
# id, 번호, 점수 (제출 시간 순서대로 저장)
# 한 문제에 대한 여러 풀이를 제출한 경우 최고 점수가 문제에 대한 점수

# - 점수 저장 규칙 -
# 하나도 제출하지 않았다면 0점
# 팀의 최종 점수는 각 문제에 대한 점수의 총합
# 순위는 팀보다 높은 점수의 팀의 수 + 1

# - 순위 결정 규칙 -
# 점수가 같을 경우
    # 풀이 횟수가 적은 팀의 순위가 높음
# 점수 - 풀이 횟수가 같을 경우
    # 마지막 제출 시간이 더 빠른 팀의 순위가 높음
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, k, idt, m = map(int,input().split())
    answer = [[0] * (k+1) for _ in range(n+1)] # 플레이어 별 문제 리스트
    log_count = [0 for _ in range(n + 1)]  # 문제 수 기록
    last_time = [0 for _ in range(n+1)] # 마지막 제출 시간 # 역순 저장

    for i in range(m):
        team_id, j, s = map(int,input().split())
        if answer[team_id][j] <= s:
            answer[team_id][j] = s
        log_count[team_id]-=1
        last_time[team_id] = -i
    answer = [sum(value) for value in answer]

    for idx,data in enumerate(sorted([[answer[i],log_count[i],last_time[i],i] for i in range(1,n+1)],reverse=True)):
        if data[3] == idt:
            print(idx+1)
            break

