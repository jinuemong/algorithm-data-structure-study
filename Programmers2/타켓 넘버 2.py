# bfs, dfs 활용
# 타겟 넘버

answer = 0
def solution(numbers, target):
    global answer
    dfs(numbers,0,[],target)
    return answer

def dfs(numbers,i,stack,target):
    # 방법 2 스택을 만들어서 더하기
    global answer
    if len(stack) == len(numbers) and sum(stack) ==target:
        answer+=1

    if i < len(numbers): #방문 x
        dfs(numbers,i+1,stack + [+numbers[i]],target)
        dfs(numbers,i+1,stack + [-numbers[i]],target)


numbers =[1, 1, 1, 1, 1]
target = 3
print(solution(numbers,target))