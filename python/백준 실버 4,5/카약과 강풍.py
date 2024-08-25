N, S, R = map(int, input().split())

broken_Team = set(map(int, input().split()))
more_Team = set(map(int, input().split()))

answer = 0

intersection = broken_Team & more_Team
brokenTeam = sorted(list(broken_Team - intersection))
more_Team = list(more_Team - intersection)

for t in brokenTeam:
    if t-1 in more_Team:
        more_Team.remove(t-1)
    elif t+1 in more_Team:
        more_Team.remove(t+1)
    else:
        answer += 1

print(answer)
