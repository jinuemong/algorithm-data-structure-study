

# 가장 큰 수
# numbers의 길이 : 1이상 100000이하
# 문자열로 리턴
# 주어진 수들을 조합해서 가장 큰 수 만들기
# 방법 3

# if 300 30 3
# 330300 -> 베스트 [3,30,300]
# if 310 31 3
# 331310 -> 베스트 [3,31,310]
# 앞자리 같을 수록 역순이 더 큼
# 3 31 32
# 33231 -> 베스트 [3,32,31]..
# 순서 : 일의자리 기준으로 역순 정렬
# 정렬된 것의 같은 자리수 기준으로 역순 정렬
# 자리수가 작은게 먼저, 자리수가 같다면 값이 큰게 먼저
# 방법 : 1의자리 순 정렬 -> 내부에서 자리수 작은 순 정렬 -> 자리수 같다면 값이 큰 순 정렬

def solution(numbers):
    numbers =sorted(numbers,key=lambda x: (-int(str(x)[0]),int(len(str(x))),-x))
    print(numbers)
    return ''.join([str(number) for number in numbers])


print(solution([3, 30, 34, 5, 9]))
