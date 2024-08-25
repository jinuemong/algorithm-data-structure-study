

# 중복 순열 구하기

from itertools import permutations
def solution(numbers):
    answer ,num_list = 0, []
    for i in range(1,len(numbers)+1):
        for j in list(permutations(list(numbers),i)):
            num_list.append(int("".join(list(j))))
    max_num, num_list = max(num_list),set(num_list) # 중복 제거 + 가장 큰 값 저장
    so_list ,m = [False if i<2 else True for i in range(max_num+1)],int(max_num**0.5)
    for i in range(2,max_num+1):
        if so_list[i]:
            for j in range(2*i,max_num+1,i):
                so_list[j]=False
    return len([i for i in num_list if so_list[i]])

print(solution("17"))