
# 트리 탐색

class Node:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right

# 전위
def pre_order(node):
    print(node.data,end ='')
    if node.left !='.':
        pre_order(tree[node. left])
    if node.right != '.':
        pre_order(tree[node.right])

# 중위
def in_order(node):
    if node.left !='.':
        in_order(tree[node.left])
    print(node.data,end='')
    if node.right !='.':
        in_order(tree[node.right])

def post_order(node):
    if node.left !='.':
        post_order(tree[node.left])
    if node.right !='.':
        post_order(tree[node.right])
    print(node.data, end='')

n = int(input())
tree ={}
for i in range(n):
    data,left,right = list(input().split())
    tree[data] = Node(data,left,right)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
