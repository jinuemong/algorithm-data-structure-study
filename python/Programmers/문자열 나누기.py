
# 문자열 나누기
# x : 첫 문자
# 첫 문자를 기준으로 x와 같은 값 = x와 다른 값이 될 때까지 횟수 체크
# 두 횟수가 같아지는 순간 문자열을 분리
# 분리한 문자열을 빼고 남은 부분에 대해서 반복
# 남은 부분이 없을 때까지 반복
# 분리된 문자열의 개수를 리턴

def solution(s):
    answer = 0
    count_x, count_y, index, x = 1, 0, 0, s[0]
    while index < len(s):

        if s[index] == x:
            count_x += 1
        else:
            count_y += 1


        if count_x == count_y:
            answer += 1
            count_x, count_y, x = 1, 0, s[index]
            index += 1
        index += 1
    return answer


s = "banana"
print(solution(s))
