

# 쿼드 압축 후 개수 세기

# 0,1 로만 이루어진 2차원 정수 2^n * 2^n
# 압축하고자 하는 영역 S
# S 내부에 있는 모든 수가 같은 값이라면, S를 해당 수 하나로 압축
# 그렇지 않다면 S를 정확히 4개의 균일한 정사각형 영역으로 쪼갠 뒤,
# 각 정사각형 영역에 같은 방식으로 압축 시도

# 더이상 압축이 불가능 하다면 갯수 출력
# 방법 구상
# 우선 개수를 카운트, 압축한 만큼 마이너스 형식
# 개수가 1일 때 까지 실행
# 재귀함수 사용

# -> 오래 걸림



answer = [0,0]
def solution(arr):
    global answer
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]==0:
                answer[0]+=1
            else:
                answer[1]+=1
    zip_arr(arr)
    return answer
def zip_arr(arr):
    if len(arr)<=1:
        return
    count_0 = arr.count(0)




print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))