
## 결승전을 통과한 순서대로 점수를 받음
# 가장 낮은 점수를 얻은 팀이 승
# 팀 점수는 상위 네 명의 주자의 점수를 합

## 6명의 주자가 참가하지 못한 팀은 점수 계산 제외
# 동점의 경우 5번째 주자가 빨리 들어온 팀이 우승

## 상위 5명을 구하고, 4명의 합으로 점수를 나눔
# 총 6명이 아닌 경우 제명

# 점수는 n/a를 제외하고 산정

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    non_count_team = set()
    count_team = {}
    for i in range(1,max(arr)+1):
        if arr.count(i) < 6:
            non_count_team.add(i)
        else:
            count_team[i] = []
    count = 1
    score = [0]*len(arr)
    for idx,team in enumerate(arr):
        if team not in non_count_team:
            score[idx] = count
            count+=1
            count_team[team].append(idx)
    first_team_num,first_team_count, first_team_five_num = 1,200*6,201
    for team_key,team_idx in count_team.items():
        team_score = sorted([score[idx] for idx in team_idx])
        result_score = sum(team_score[0:4])
        if result_score < first_team_count \
                or (result_score == first_team_count and first_team_five_num > team_score[4]):
            first_team_num = team_key
            first_team_count = result_score
            first_team_five_num = team_score[4]

    print(first_team_num)