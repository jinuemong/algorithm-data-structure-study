
# 큰 수 만들기
# k개의 수를 제거했을 때 얻을 수 있는 가장 큰 수 구하기
# 1924 -> 1,2 제거 후 94
# 작은 숫자 k개 제거, 큰 숫자 순서대로 k개 출력
# 기존의 순서는 유지되어야 함 !

# 문제 ! 적은 수로 커트하면,안됨
# 가장 큰 수가 앞에 올 수 있도록 앞자리 수를 제거해야 함
# 제거한 경우의 수를 만들기에는 너무 큼


from collections import Counter
def solution(number, k):
    data,number = Counter(sorted(number)[:len(number)-k]),list(number)

    for i in range(len(number)):
        if number[i] in data and data[number[i]]>0:
            k-=1
            data[number[i]]-=1
            number[i] = ""
        if k == 0:
            return "".join(number)

number = "4177252841"
k = 4
print(solution(number,k))


# 4177252841
# 775841
# 4 1 2 2 제거