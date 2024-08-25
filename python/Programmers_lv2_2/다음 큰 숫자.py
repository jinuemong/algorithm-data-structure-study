

# 다음 큰 숫자
# n보다 큰 자연수
# 2진수로 변환했을 때 1의 갯수가 같다
# n 다음으로 오는 가장 작은 수

def solution(n):
    n_jinsu,i = jinsu(n),n
    while True:
        i +=1
        if jinsu(i)==n_jinsu:
            return i
def jinsu(k):
    count = 0
    while k > 0:
        if k%2==1:
            count+=1
        k = k//2
    return count
print(solution(78))
