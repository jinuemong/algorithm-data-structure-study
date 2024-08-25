

# 두 개 이하로 다른 비트

# f(x) : x보다 크고 x와 비트가 1~2개 다른 수들 중에서 제일 작은 수
# 경우의 수가 많으므로 최적의 알고리즘을 구해야 함
# xor 연산을 통해서 서로 다른 수를 찾을 수 있다
# -> 값이 다를 경우 트루
# 연산 후 해당 값의 합이 2보다 작거나 같아야 함

# 비트 연산으로 풀면 시간 초과 발생
# 숫자가 짝수인 경우 항상 마지막 비트는 0이므로, 하나의 비트 차이가 나는 경우는 +1 이다
# 홀수인 경우 가장 뒤의 0을 1로 바꾸고 그 다음 비트를 0으로 바꾼 경우가 답이다
# 즉 0이 나타난 부분을 1로 바꾸고, 그 뒤를 0으로 바꾸면 가장 작은 수를 찾게 된다.
# 규칙을 적용해서 문제를 푼다
def solution(numbers):
    answer = []
    for number in numbers:
        if number%2 == 0:
            answer.append(number+1)
        else:
            answer.append(re_data(number,""))
    return answer

def re_data(data,answer):
    while data>0:
        answer = answer+str(data%2)
        data//=2
    answer+="0"
    idx = answer.index("0")
    answer = answer[0:idx - 1] + "01" + answer[idx + 1:]
    return int(answer[::-1],2)



print(solution([2,7]))