
# 뒤에 있는 큰 수 찾기
# 자신보다 크면서 가장 가까이 있는 수
# number의 길이가 100만까지 가능하므로, 최적 알고리즘을 사용해야 한다
# 스택을 제작
# 스택이 비었다면 스택에 데이터 추가
# 스택에 값이 있다면 다음 값과 비교
# 값이 더 크다면 뒤큰수 발견 -> 스택에 있는 인덱스들의 값 변경
# 값이 작거나 같다면 스택에 추가

# 기록된 인덱스로 정렬

def solution(numbers):
    stack = []
    for i in range(len(numbers)):
        if len(stack) == 0:
            stack.append(i)
        else:
            if numbers[stack[0]] < numbers[i]: #뒤큰수 발견
            
                for j in range(len(stack)):
                    numbers[stack[j]] = numbers[i]
                stack = [i]
            else:
                stack.append(i)
    for i in stack:
        numbers[i] = -1
    return numbers

numbers = [2, 3, 3, 5]
print(solution(numbers))