

# 가장 큰 수
# numbers의 길이 : 1이상 100000이하
# 문자열로 리턴
# 주어진 수들을 조합해서 가장 큰 수 만들기
# 1의 자리 순으로 정렬
# 해당 순번대로 출력
# 9와 89비교
# 989 , 899 -> 9가 더 큼
# 8와 89비교
# 889 898 -> 89가 더 큼
# 숫자를 분해해서 리스트에 넣기
# 후 정렬
def solution(numbers):
    for i in range(len(numbers)):
        numbers[i] = list(map(int,str(numbers[i])))
    numbers.sort(reverse=True)
    print(numbers)
    return ''.join([''.join(list(map(str,number))) for number in numbers])

print(solution([3, 30, 34, 5, 9]))
