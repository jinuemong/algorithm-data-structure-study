

# 자주 사용하는 모든 함수 정리
# 큐 - 선입 선출
import queue
data = queue.Queue()
print(type(data))
data.put(2)
data.put(3)
data.put(4)
print(data.get())
print(data.get())
print(data.get())

# 스택 - 후입 선출
stack = []
stack.append(2)
stack.append(3)
stack.append(4)
print(stack.pop())
print(stack.pop())
print(stack.pop())


# 2차원 배열 관련

## 배열 뒤집기
array = [[i for i in range(4)] for j in range(5)]
print(array)
new_array = list(map(list,zip(*array)))
print(new_array)

## 특정 인덱스 기준 정렬
array = [[1,2,1],[2,4,1],[5,4,2],[1,1,4]]
print(array)
array.sort(key = lambda data : data[1]) #2번째 인덱스 기준 정렬
print(array)

# 다중 기준 정렬
# 평소 -> 0번 인덱스 기준 , 아래 예시 -> 0,1번 인덱스 기준
print(sorted(array,key = lambda x:  (x[0],x[1])))

# 문자열에서 특정 문자 삭제
import re
string = "AA**BB#@$CC 가나다-123"
# 0 - 9 제거
print(re.sub(r"[0-9]","",string))
# 알파벳만 남기기
string = "AA**BB#@$CC 가나다-123"
print(re.sub(r"[^a-zA-Z]", "", string))

# DRF, BFS 자료
root_node = 1
graph_list = {
    1: set([3,4]),
    2: set([3,4,5]),
    3 :set([1,5]),
    4 :set([1]),
    5 :set([2,6]),
    6: set([3,5]),
}

# DFS 깊이 우선 탐색
def DFS(graph, root): # stack
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack+= graph[n] - set(visited)
    return visited
print("DFS : ",DFS(graph_list,root_node))

# BFS 너비 우선 탐색
from collections import  deque
def BFS(graph, root): # deque
    visited = []
    queue = deque([root])
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited
print("BFS : ",BFS(graph_list,root_node))

# 중복 순열 # (1,1) 가능
from itertools import product
data = ["1","2","3"]

print(list(product(data,repeat = 2)))

# 순열 (ab != ba)
from itertools import permutations
print(list(permutations(data,2)))

# 조합 ( ab == ba)
from itertools import combinations
print(list(combinations(data,2)))

# 중복 조합 # (1,1) 가능
from itertools import combinations_with_replacement
print(list(combinations_with_replacement(data,2)))