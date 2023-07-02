

# 숫자 변환하기
# 자연수 x를 y로 변환
# x + n , x * 2 , x * 3
# x,y가 100만까지 가능
# 최소 연산으로 x를 y로 변환
# 방정식 사용
# 3*a*x + 2*b*x + cn = y를 만족하는 값을 찾아야 한다
# 2,5,4 대입 : 6a + 4b + 4c = 5를 만족
# a,b,c는 *2,*3,+n의 갯수
# a의 범위 : (0~(y//3*x))
# b의 범위 : (0~(y//2*x))
# c의 범위 : (0~(y//n))

def solution(x, y, n):
    result = -1
    for a in range(0, y//(3*x) + 2):
        for b in range(0, y//(2 * x) + 2):
            for c in range(0, y//n + 2):
                if 3*a*x+2*b*x+c*n ==y or x+c*n==y:
                    answer = a+b+c
                    if answer<result or result==-1:
                        result = answer
    return result


print(solution(10,40,30))