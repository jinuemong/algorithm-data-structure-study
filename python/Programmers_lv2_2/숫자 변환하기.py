

# 숫자 변환하기
# 자연수 x를 y로 변환
# x + n , x * 2 , x * 3
# x,y가 100만까지 가능하므로 중첩문으로 해결 불가능
# 최소 연산으로 x를 y로 변환

result = -1
def solution(x, y, n):
    global result
    search(x,y,n,0)
    return result
def search(x,y,n,count):
    global result
    if x==y and (result==-1 or count<result):
        result = count
    elif (result<1 or count < result) and x<y:
        search(x * 2, y, n, count + 1)
        search(x * 3, y, n, count + 1)
        search(x + n, y, n, count + 1)

print(solution(2,5,4))