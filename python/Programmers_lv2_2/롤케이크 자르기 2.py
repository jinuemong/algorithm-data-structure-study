

# 롤케이크 자르기
# 공평한 롤케이크
# 1,2,3,4 : 토핑의 종류
# 토핑이 있는 케이크를 자를 때 좌, 우 토핑의 종류가 같아야 함
# 공평하게 자르는 경우의 수 리턴
# 공평하게 자를 수 없을 경우 0 리턴
# 두 조각으로 나눠야 하므로 정확하게 반으로 나눠야 함
# 문제풀이
# 반으로 자른 후 좌,우 확인
# 더 토핑이 많은쪽으로 이동
# deque 활용

from collections import deque
def solution(topping):
    answer = 0
    left_topping,topping =set(),deque(topping.copy())
    while topping:
        left_topping.add(topping.popleft())
        if len(left_topping) == len(set(topping)):
            answer+=1
    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2]	))