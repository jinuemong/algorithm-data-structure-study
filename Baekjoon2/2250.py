
# 트리의 높이와 너비

# 조건 1> 같은 레벨의 노드는 같은 행에 위치
# 조건 2> 한 열에는 한 노드만 존재
# 조건 3> 임의의 노드 왼쪽 노드들은 해당 노드보다 왼쪽에 위치, 오른쪽 노드는 오른쪽
# 조건 4> 노드가 배치된 가장 왼쪽 열과 오른쪽 열 사이엔 아무 노드도 없이 비어있는 열은 없다.

# 문제 풀이 방법 ! 노드를 생성하고, 중위 순회 통해서 가장 좌측의 노드부터 칸을 채움
# 왼쪽부터 칸을 채우는 중위 순회를 할 경우 열번호가 왼쪽 값보다 오른쪽 값이 항상 큼
# deep을 리스트를 만들어서 노드 리스트를 생성하고 가장 작은값 가장 큰 값 차이를 계산



class Node:
    def __init__(self,data,left,right):
        self.parent = -1 # 루트 노드를 찾기 위함
        self.data = data
        self.left = left
        self.right = right

def in_order(node,col):
    global row
    if node.left!=-1 or node.right!=-1:
        col +=1
    if node.left != -1:
        in_order(tree[node.left],col)
    ## 중위 탐색 ##
    if node.left==-1 and node.right==-1:
        col += 1
    array[col].append(row)
    row+=1
    ## #### ##
    if node.right != -1:
        in_order(tree[node.right],col)



n = int(input())

tree = {}
array = [[] for i in range(0,n+1)]
row = 1


for i in range(1,n+1): #기존 트리를 생성해야 루트 노드를 찾을 수 있음
    tree[i] = Node(i,-1,-1)

for _ in range(n):
    data,left,right = list(map(int,input().split()))
    tree[data].left = left
    tree[data].right = right
    if left != -1:
        tree[left].parent = data
    if right != -1:
        tree[right].parent = data

for i in range(1, n+1):
    if tree[i].parent == -1: #루트
        in_order(tree[i],0)

level,width =0,0
for i in range(1,n+1):
    array_len = int(len(array[i]))
    if array_len==0:
        break
    elif array_len==1: #데이터가 하나인 경우
        if width<1:
            width = 1
            level = i
    else: # 데이터가 여러개인 경우 : 맨 끝 - 맨 처음
        new_width = array[i][-1] - array[i][0] + 1
        if width <new_width: #같은 경우는 조사안해도 됨 -> 맨 처음이 최소 레벨
            width = new_width
            level = i

print(level,width)
  