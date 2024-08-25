
# 트리 순회

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class NodeManage:
    def __init(self,head):
        self.head = head

    def insert(self,value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left!=None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right!=None:
                    self.current_node=self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break