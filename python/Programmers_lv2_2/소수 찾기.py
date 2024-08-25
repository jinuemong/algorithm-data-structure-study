

# 중복 순열 구하기

from itertools import permutations
def solution(numbers):
    answer = 0
    data_set = []
    for i in range(1, len(numbers) + 1):
        for k in permutations(list(numbers),i):
            data_set.append(int("".join(list(k))))
    max_data, data_set= max(data_set),set(data_set)

    so_list = [True for _ in range(max_data+1)]
    so_list[0],so_list[1],m = False,False,int(max_data**0.5) # 루트까지 값만 조사
    for i in range(2,m+1):
        if so_list[i] == True:
            for j in range(2*i,max_data+1,i):
                so_list[j] = False

    return len([i for i in data_set if so_list[i]])

print(solution("011"))