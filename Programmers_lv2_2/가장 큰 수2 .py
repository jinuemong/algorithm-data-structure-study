

# 가장 큰 수
# numbers의 길이 : 1이상 100000이하
# 문자열로 리턴
# 주어진 수들을 조합해서 가장 큰 수 만들기
# 방법 2
#  조합 리스트 넣기
# 가장 큰 수를 출력
# -> 시간 초과
from itertools import permutations

def solution(numbers):
    max = 0
    for number in permutations(numbers,len(numbers)):
        data = int(''.join(list(map(str,number))))
        if data>max:
            max = data
    return str(max)

print(solution([3, 30, 34, 5, 9]))
