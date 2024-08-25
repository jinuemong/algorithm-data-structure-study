

n, m = list(map(int,input().split()))  # n : 사람 수, m : 파티 수
know_man = set(list(map(int,input().split()))[1:]) # 진실을 아는 사람 모임
count = 0
party_list = [list(map(int,input().split()))[1:] for _ in range(m)] # 파티 리스트

for _ in range(m):
    for party in party_list:
        if set(party) & know_man:
            know_man = know_man | set(party)

for party in party_list:
    if set(party) & know_man:
        continue
    count+=1
print(count)