

# bfs, dfs 활용
# 타겟 넘버

answer = 0
def solution(numbers, target):
    global answer
    visited = [False]*len(numbers)
    dfs(numbers,visited,0,target)
    return answer

def dfs(numbers,visited,sum,target):
    global answer
    if sum ==target:
        answer+=1
    for i in range(len(numbers)):
        if not visited[i] and target>sum: #방문 x
            print(visited)
            visited[i] = True
            dfs(numbers,visited,sum+numbers[i],target)
            dfs(numbers,visited,sum-numbers[i],target)
            visited[i] = False # 다른 탐색을 위해서 복귀

numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers,target))