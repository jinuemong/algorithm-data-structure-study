
# 두 수의 최소공배수
# 배수 중 공통이 되는 가장 작은 수
# n개의 수들의 최소 공배수를 구하라
# 가장 큰수로 나눌 수 있는지

def solution(arr):
    max_data ,not_find = max(arr) , True
    while not_find:
        for i in arr:
            if max_data%i==0 and max_data!=i:
                not_find = False
            else:
                not_find = True
        max_data*=2

    return max_data

print(solution([1,2,3]))

