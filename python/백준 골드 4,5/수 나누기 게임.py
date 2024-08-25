# 수 나누기 게임
# 나머지 0 -> 한 족이 다른 수의 배수
# n = int(input())
# answer = [0] * n
# l = list(map(int, input().split()))
#
# for i in range(0, n - 1):
#     cur = l[i]
#     for j in range(i + 1, n):
#         enemy = l[j]
#
#         if enemy % cur == 0:
#             answer[i] += 1
#             answer[j] -= 1
#
#         elif cur % enemy == 0:
#             answer[i] -= 1
#             answer[j] += 1
#         else:
#             pass
# print(answer)

n = int(input())
cards = list(map(int,input().split()))

cards_with_idx = {card : idx for idx, card in enumerate(cards)}
max_card = max(cards)
res = [0] * n

for i in range(n):
    current = cards[i]
    for j in range(current*2 , max_card+1,current):
        if j in cards_with_idx:
            idx = cards_with_idx[j]
            res[i] +=1
            res[idx] -=1
for i in res:
    print(i,end = ' ')