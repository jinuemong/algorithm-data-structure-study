

# 자신 바로 앞의 선수를 추월할 때 이름 호출
# players  : 5~ 50000
# call : < 1000000

# 딕셔너리 활용한 정렬 -> 시간복잡도 감소
# 통과 !

def solution(players, callings):
    players_dic = {}
    # 순서 기록
    for i in range(len(players)):
        players_dic[players[i]] = i

    for calling in callings:
        # 딕셔너리를 활용한 방법
        index = players_dic[calling]
        prev = players[index-1]
        players_dic[prev] = index
        players_dic[calling] = index-1

        players[index] = players[index-1]
        players[index-1] = calling
    return players


players = input().split(",")
callings = input().split(",")
solution(players,callings)