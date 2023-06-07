
# 시간초과

# 자신 바로 앞의 선수를 추월할 때 이름 호출
# players  : 5~ 50000
# call : < 1000000

def solution(players, callings):

    for calling in callings:
        index = players.index(calling)
        players[index] = players[index-1]
        players[index-1] = calling
    return players


players = input().split(",")
callings = input().split(",")
solution(players,callings)