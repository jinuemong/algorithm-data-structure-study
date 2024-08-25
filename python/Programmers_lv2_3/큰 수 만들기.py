
# 큰 수 만들기
# k개의 수를 제거했을 때 얻을 수 있는 가장 큰 수 구하기
# 1924 -> 1,2 제거 후 94
# 작은 숫자 k개 제거, 큰 숫자 순서대로 k개 출력
# 기존의 순서는 유지되어야 함 !

# 오래걸리는 문제 풀이 1
# 정렬 후 컷투
from collections import Counter
def solution(number, k):
    data,number = Counter(sorted(number)[:k]),list(number)
    for i in range(len(number)):
        if number[i] in data and data[number[i]]>0:
            data[number[i]]-=1
            number[i] = " "
    print(data)
    return "".join(number).replace(" ","")

number = "4177252841"
k = 4
print(solution(number,k))
