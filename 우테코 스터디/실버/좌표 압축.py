

# 좌표 압축
# 정렬 후 인덱스를 키로 가지는 딕셔너리 생성
# 각 리스트를 돌면서 값에 맞는 인덱스를 출력

import sys
n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
n_list2 = list(sorted(set(n_list)))

dic = {value: index for index, value in enumerate(n_list2)}

for e in n_list:
    print(dic[e],end=" ")