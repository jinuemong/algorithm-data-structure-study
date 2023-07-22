

# 쿼드 압축 후 개수 세기

# 0,1 로만 이루어진 2차원 정수 2^n * 2^n
# 압축하고자 하는 영역 S
# S 내부에 있는 모든 수가 같은 값이라면, S를 해당 수 하나로 압축
# 그렇지 않다면 S를 정확히 4개의 균일한 정사각형 영역으로 쪼갠 뒤,
# 각 정사각형 영역에 같은 방식으로 압축 시도


# 4개씩 합쳤을 때, 합치지 못한 부분은 다시 사용 못함

x,y = 0,0
def solution(arr):
    global x,y
    quad(arr,True)

    return [x,y]

def quad(arr,first):
    global x,y
    new_arr = [[0]*(len(arr)//2) for _ in range((len(arr)//2))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j]==0:
                if first:
                    x+=1
                new_arr[i//2][j//2]-=1
            elif arr[i][j]==1:
                if first:
                    y+=1
                new_arr[i//2][j//2]+=1
    if len(new_arr)<=1:
        return [x,y]

    for i in range(len(new_arr)):
        for j in range(len(new_arr)):
            if new_arr[i][j] == -4 :
                new_arr[i][j] = 0
                x-=3
            elif new_arr[i][j]== 4:
                new_arr[i][j] = 1
                y-=3
            else:
                new_arr[i][j] = 2**10
    quad(new_arr,False)

# arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
print(solution(arr))