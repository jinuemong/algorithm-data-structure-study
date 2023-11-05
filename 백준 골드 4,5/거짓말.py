

# 문제 이해
# 지민이는 거짓말을 해야 하며
# 이야기를 아는 사람에게 말을 하면 거짓말이 걸림
# 한 사람이 여러 파티에 참여한 경우가 있으며, 진실을 말할수도있고, 거짓을 말할 수도 있다
# 거짓말한 경우에만 해당 사람들을 추가

n, m = list(map(int,input().split()))  # n : 사람 수, m : 파티 수
x_man = set(list(map(int,input().split()))[1:]) # 진실을 아는 사람 모임
n_x_man = set()
count = 0
party_list = [list(map(int,input().split()))[1:] for _ in range(m)] # 파티 리스트
for party in party_list:
    non_x_man  = 0
    for man in party:
        if man not in x_man:
            non_x_man+=1
    if non_x_man==len(party):
        print(party,x_man)
        for man in party:
            x_man.add(man)
        count+=1
print(count)