

# 그림 교환


# 그림을 팔 때, 그림을 산 가격보다 크거나 같은 가격으로 팔아야 한다.
# 같은 그림을 두 번 이상 사는 것은 불가능하다.
# i번째 에술가에게 j번째 예술가가 지불한 금액 -> 리스트

import sys
input = sys.stdin.readline

max_len = 0
n = int(input()) # 2~ 15
n_list = dict()
for i in range(n):
    new = input().strip()
    for j in range(len(new)):
        if j != i:
            if int(new[j]) in n_list:
                n_list[int(new[j])].append((j,i))
            else:
                n_list[int(new[j])] = [(j,i)]

start = n_list[min(n_list.keys())]
for s in start:
    owner = set()
    owner.add(s[0])
    print(owner)
print(start)



# def search(owner,depth,current):
#     for data in n_list[depth]:
#         if current == data[0]:
#             if current not in owner and depth+1 in n_list:
#                 search(owner+current,depth+1,data[1])
#                 max_len = max(len(owner),max_len)
# print(max_len)
