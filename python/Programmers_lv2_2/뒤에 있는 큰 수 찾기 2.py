# 뒤에 있는 큰 수 찾기
# 자신보다 크면서 가장 가까이 있는 수
# number의 길이가 100만까지 가능하므로, 최적 알고리즘을 사용해야 한다
# 스택을 제작
# 스택이 비었다면 스택에 데이터 추가
# 스택에 값이 있다면 스택의 마지막 값과 비교
# 반복문으로 더 큰값이 나오는 동안 스택의 마지막 값 pop해서 변경
# 값이 더 크다면 뒤큰수 발견 -> 스택에 있는 인덱스의 값 변경
# 뒤로 가는 중에 값이 작거나 같다면 오큰수가 없으므로 stop
# 현재 값을 stack에 추가
# 종료 후 스택에 있는 값들을 -1로 변경
# 기록된 인덱스로 정렬

def solution(numbers):
    stack = []
    for i in range(len(numbers)):
        while stack:
            if numbers[stack[-1]]<numbers[i]:
                numbers[stack.pop()] = numbers[i]
            else:
                break
        stack.append(i)
    for i in stack:
        numbers[i] = -1
    return numbers


numbers = [9, 1, 5, 3, 6, 2]

print(solution(numbers))