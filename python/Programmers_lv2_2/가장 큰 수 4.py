

# 가장 큰 수
# numbers의 길이 : 1이상 100000이하
# 문자열로 리턴
# 주어진 수들을 조합해서 가장 큰 수 만들기
# 방법 4
# 모든 수가 1000의 자리 수 이하이므로
# 가장 작은 수를 3자리로 만들어서 비교


def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key = lambda x:x*3,reverse=True)
    return str(int(''.join(numbers)))


print(solution([3, 30, 34, 5, 9]))
